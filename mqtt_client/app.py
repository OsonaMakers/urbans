from src.MQTTClient import MQTTClient
from src.DB import DB
import logging
from dotenv import load_dotenv
from os import getenv

load_dotenv()

debug_level = logging.WARNING if getenv(
    'ENV') == 'production' else logging.DEBUG
logging.basicConfig(level=debug_level)

if __name__ == '__main__':
    db = DB()
    client = MQTTClient()

    def on_message(client, userdata, msg):
        print(f"TOPIC: [{msg.topic}] -- {msg.payload.decode()}")
        db.insert(msg.topic, {"data": msg.payload.decode()})

    client.connect()
    client.subscribeToAllTopics()
    # client.subscribe('**/**')
    # client.publish('**/**', '***F')
    client.setOnMessage(on_message)
    client.loop_forever()
