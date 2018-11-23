from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import datetime

class KlimaSkill(MycroftSkill):

    def __init__(self):
        super(KlimaSkill, self).__init__(name="KlimaSkill")

    @intent_handler(IntentBuilder("").require("temperatur"))
    def handle_temperatur_intent(self, message):
        self.speak_dialog("temperatur")

def create_skill():
    return KlimaSkill()
