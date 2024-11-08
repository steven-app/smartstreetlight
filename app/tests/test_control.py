import pytest
from app.services.mqtt_service import MqttService

def test_turn_on_light():
    response = MqttService.publish("light/control", {"status": "on"})
    assert response == "Message sent"

def test_turn_off_light():
    response = MqttService.publish("light/control", {"status": "off"})
    assert response == "Message sent"
