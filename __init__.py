from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import datetime
import requests

class KlimaSkill(MycroftSkill):

    def __init__(self):
        super(KlimaSkill, self).__init__(name="KlimaSkill")

    @intent_handler(IntentBuilder("GetTemperaturIntent").require("getTemperature").require("room").build())
    def handle_get_temperature_intent(self, message):
        print(message.data)
        raum = message.data.get("room")
        print(raum)
        raum = raum.title()
        print(raum)
        api_url = "http://openhab-test.synyx.coffee:8080/rest/items/%s_Temperature_Current" % (raum)
        r = requests.get(api_url)
        temperature = r.json()["state"]
        self.speak_dialog("getTemperature", data={"temperature": temperature})

    @intent_handler(IntentBuilder("SetTemperaturIntent1").require("setTemperature").require("temperature").require("grad").require("room").build())
    def handle_set_temperature_intent(self, message):
        print(message.data)
        temperature = message.data.get("temperature")
        room = message.data.get("room")
        room = room.title()
        api_url = "http://openhab-test.synyx.coffee:8080/rest/items/%s_Temperature_Target" % (room)
        requests.post(api_url, data=temperature)
        self.speak_dialog("setTemperature", data={"temperature": temperature, "room": room})

    @intent_handler(IntentBuilder("PenisIntent").require("penis").build())
    def handle_set_temperature_intent(self, message):
        self.speak_dialog("penis")

def create_skill():
    return KlimaSkill()
