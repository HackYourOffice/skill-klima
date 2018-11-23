from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import datetime
import requests

class KlimaSkill(MycroftSkill):

    def __init__(self):
        super(KlimaSkill, self).__init__(name="KlimaSkill")

    @intent_handler(IntentBuilder("").require("foobar"))
    def handle_set_temperature_intent(self, message):
        print(message.data)
        temperature = message.data.get("temperature")
        print(temperature)
        self.speak_dialog("setTemperature", data={"temperature": temperature})

def create_skill():
    return KlimaSkill()
