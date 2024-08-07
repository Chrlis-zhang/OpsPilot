from apps.bot_mgmt.services.skill_excute_service import SkillExecuteService
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView


class SkillExecuteView(APIView):
    @swagger_auto_schema(
        operation_id="skill_execute",
        operation_description="",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "bot_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="机器人ID"),
                "skill_id": openapi.Schema(type=openapi.TYPE_STRING, description="技能ID"),
                "user_message": openapi.Schema(type=openapi.TYPE_STRING, description="用户消息"),
                "chat_history": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    description="历史对话",
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                ),
            },
            required=[
                "bot_id",
                "skill_id",
                "user_message",
            ],
        ),
    )
    def post(self, request, format=None):
        bot_id = request.data.get("bot_id")
        skill_id = request.data.get("skill_id")
        user_message = request.data.get("user_message")
        sender_id = request.data.get("sender_id", "")
        converation_history = request.data.get("chat_history", [])
        enable_online_search = request.data.get("enable_online_search", False)

        service = SkillExecuteService()
        result = service.execute_skill(bot_id, skill_id, user_message, converation_history, sender_id,
                                       enable_online_search)

        return JsonResponse({"result": result})
