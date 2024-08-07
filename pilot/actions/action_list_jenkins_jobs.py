from typing import Text, Any, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from eventbus.automation_eventbus import AutomationEventbus


class ActionListJenkinsJobs(Action):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> Text:
        return "action_list_jenkins_jobs"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        eventbus = AutomationEventbus()
        eventbus.publish_automation_event("list_jenkins_jobs",
                                          tracker.sender_id, tracker.get_latest_input_channel())
