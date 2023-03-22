import logging
import random
import string
from os import getenv
import paho.mqtt.client as paho
from paho import mqtt


class MQTTClient:
    def __init__(self, client_id=None, keepalive=60):
        self._validateEnv()
        self.broker = getenv("MQTT_BROKER")
        self.port = int(getenv("MQTT_PORT", 1883))
        self.username = getenv("MQTT_USERNAME")
        self.password = getenv("MQTT_PASSWORD")
        client_id = client_id if client_id != None else self._generateRandomId()
        self.keepalive = keepalive
        self.client = paho.Client(
            client_id=client_id,  protocol=paho.MQTTv5)

        self.client.username_pw_set(self.username, self.password)
        self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self.client.tls_insecure_set(True)

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message

    def _validateEnv(self):
        requireds = [
            "MQTT_BROKER",
            "MQTT_PORT",
            "MQTT_USERNAME",
            "MQTT_PASSWORD",
        ]
        for required in requireds:
            if getenv(required) is not None:
                continue
            raise Exception(f"Falta definir la variable {required}")

    def _generateRandomId(self, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length)) + '-mqqtClient'

    def on_connect(self, *args):
        logging.debug(
            f"Connectat amb el broker MQTT {self.broker}:{self.port}")

    def on_disconnect(self, client, userdata, rc, *args):
        if rc == 0:
            logging.debug("Client desconnectat correctament")
        else:
            logging.error(f"Client desconnectat amb el codi error {rc}")
            logging.debug(args)

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        logging.debug(f"Subscrit a {mid}F")

    def on_message(self, client, userdata, msg):
        print(f"TOPIC: [{msg.topic}] -- {msg.payload.decode()}")

    def connect(self):
        logging.debug(
            f":: Intentant connectar amb {self.broker}:{self.port} ttl {self.keepalive}")
        try:
            self.client.connect(self.broker, self.port, self.keepalive)
        except Exception as e:
            logging.error(":: Error en connectar ::")
            logging.error(e)
            exit()

    def subscribe(self, topic, qos=1):
        logging.debug(f"Intentant subscriure al topic {topic}")
        self.client.subscribe(topic, qos=qos)

    def subscribeToAllTopics(self):
        self.subscribe("#")

    def publish(self, topic, payload, qos=1):
        logging.debug(f"Enviant payload al topic {topic}")
        self.client.publish(topic=topic, payload=payload, qos=qos)

    def loop_forever(self):
        self.client.loop_forever()

    def setOnMessage(self, cb):
        self.client.on_message = cb
