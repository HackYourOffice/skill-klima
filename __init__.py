from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import datetime
import requests

class KlimaSkill(MycroftSkill):

    def __init__(self):
        super(KlimaSkill, self).__init__(name="KlimaSkill")

    @intent_handler(IntentBuilder("").require("temperatur"))
    def handle_temperatur_intent(self, message):
        print(message.data)
        raum = message.data["raum"]
        print(raum)
        raum = raum.title()
        print(raum)
        api_url = "http://openhab-test.synyx.coffee:8080/rest/items/%s_Temperature_Current" % (raum)
        r = requests.get(api_url)
        temperatur = r.json()["state"]
        self.speak_dialog("temperatur", data={"temperatur": temperatur})

def create_skill():
    return KlimaSkill()
