from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCustomReply(Action):

    def name(self) -> Text:
        return "action_custom_reply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get("text")
        reply = f"You just typed: {user_message}"

        dispatcher.utter_message(text=reply)
        return []

class ActionGreetWithName(Action):

    def name(self) -> Text:
        return "action_greet_with_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if name:
            dispatcher.utter_message(text=f"Hello, {name}! How can I help you with your shopping today?")
        else:
            dispatcher.utter_message(text="Hello! How can I help you with your shopping today?")

        return []

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Ok... \nDone!\nGoodbye! Have a great day.")
        return []
