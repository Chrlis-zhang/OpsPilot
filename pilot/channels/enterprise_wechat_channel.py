import asyncio
import inspect
import os
from typing import Dict, Optional, Text, Any, Callable, Awaitable

from logging import getLogger
from rasa.core.channels.channel import (
    InputChannel,
    CollectingOutputChannel,
    UserMessage,
)
from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from wechatpy.enterprise import WeChatClient, WeChatCrypto, parse_message

from utils.eventbus import EventBus

logger = getLogger(__name__)


class EnterpriseWechatChannel(InputChannel):
    def name(self) -> Text:
        return "enterprise_wechat"

    def __init__(self, corp_id, secret, token, aes_key, agent_id, enable_eventbus) -> None:
        super().__init__()

        self.corp_id = corp_id
        self.secret = secret
        self.token = token
        self.aes_key = aes_key
        self.agent_id = agent_id

        self.crypto = WeChatCrypto(token, aes_key, corp_id)

        self.wechat_client = WeChatClient(
            corp_id,
            secret,
        )

        self.bot_id = os.getenv('MUNCHKIN_BOT_ID', "")
        if enable_eventbus:
            queue_name = f"enterprise_wechat_{self.bot_id}"
            logger.info(f"启动Pilot消息总线:[{queue_name}]")
            self.event_bus = EventBus()
            self.event_bus.consume(queue_name, self.recieve_event)

    def recieve_event(self, event):
        if self.event_bus.is_notification_event(event):
            reply_user_id = self.event_bus.get_notification_event_sender_id(event)
            reply_text = self.event_bus.get_notification_event_content(event)
            self.wechat_client.message.send_markdown(self.agent_id, reply_user_id, reply_text)

    @classmethod
    def from_credentials(cls, credentials: Optional[Dict[Text, Any]]) -> "InputChannel":
        return cls(
            credentials.get("corp_id"),
            credentials.get("secret"),
            credentials.get("token"),
            credentials.get("aes_key"),
            credentials.get("agent_id"),
            credentials.get("enable_eventbus", False),
        )

    async def send_message(self, on_new_message, query, reply_user_id):
        try:
            if not query:
                return
            logger.info(f"[Received message]:{query}")

            context = dict()
            context['from_user_id'] = reply_user_id
            collector = CollectingOutputChannel()

            await on_new_message(
                UserMessage(
                    text=query,
                    output_channel=collector,
                    sender_id=reply_user_id,
                    input_channel=self.name(),
                    metadata=None,
                )
            )

            response_data = collector.messages
            reply_text = (
                "\n\n".join(data["text"] for data in response_data)
                .replace("bot:", "")
                .strip()
            )

            self.wechat_client.message.send_markdown(self.agent_id, reply_user_id, reply_text)
        except Exception as error:
            logger.error(error)

    def check_signature(self, signature, timestamp, nonce, echostr):
        return self.crypto.check_signature(signature, timestamp, nonce, echostr)

    def blueprint(
            self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:
        enterprise_wechathook = Blueprint(
            f"enterprise_wechat_hook_{type(self).__name__}",
            inspect.getmodule(self).__name__,
        )

        @enterprise_wechathook.route("/", methods=["GET"])
        async def index(request: Request) -> HTTPResponse:
            msg_signature = request.args.get('msg_signature')
            timestamp = request.args.get('timestamp')
            nonce = request.args.get('nonce')
            echostr = request.args.get('echostr')

            logger.info(
                f'Enterprise WeChat verification: msg_signature:{msg_signature}, timestamp:{timestamp}, nonce:{nonce}, echostr:{echostr}')

            echo_str = self.check_signature(msg_signature, timestamp, nonce, echostr)
            return response.text(echo_str)

        @enterprise_wechathook.route("/", methods=["POST"])
        async def msg_entry(request: Request) -> HTTPResponse:
            query_params = request.args
            signature = query_params.get('msg_signature', '')
            timestamp = query_params.get('timestamp', '')
            nonce = query_params.get('nonce', '')

            if request.method == 'GET':
                echostr = query_params.get('echostr', '')
                echostr = self.check_signature(
                    signature, timestamp, nonce, echostr
                )
                return echostr
            elif request.method == 'POST':
                message = self.crypto.decrypt_message(
                    request.body,
                    signature,
                    timestamp,
                    nonce
                )
                message = parse_message(message)
                if message.type == "event":
                    return HTTPResponse(body="")

                if message.type == "text":
                    asyncio.create_task(self.send_message(
                        on_new_message,
                        message.content,
                        message.source,
                    ))

                return HTTPResponse(body="")

        return enterprise_wechathook
