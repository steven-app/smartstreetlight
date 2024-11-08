import pytest
from app.models import Alert
from faker import Faker
from datetime import datetime

fake = Faker()

@pytest.fixture
def new_alert():
    alert = Alert(
        message=fake.sentence(),
        timestamp=datetime.now()
    )
    return alert

def test_new_alert(new_alert):
    assert new_alert.message is not None
    assert new_alert.timestamp is not None
