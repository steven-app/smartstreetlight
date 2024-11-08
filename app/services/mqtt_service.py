import paho.mqtt.client as mqtt
from app import current_app

class MQTTService:
    def __init__(self):
        self.client = mqtt.Client()

    def connect(self, broker_url, broker_port):
        self.client.connect(broker_url, broker_port)
        self.client.loop_start()

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def subscribe(self, topic, on_message_callback):
        self.client.subscribe(topic)
        self.client.on_message = on_message_callback

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
