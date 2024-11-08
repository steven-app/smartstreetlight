import pytest
from app.models import Device
from faker import Faker

fake = Faker()

@pytest.fixture
def new_device():
    device = Device(
        name=fake.name(),
        location=fake.address(),
        ip_address=fake.ipv4(),
        status="active"
    )
    return device

def test_new_device(new_device):
    assert new_device.name is not None
    assert new_device.ip_address is not None
    assert new_device.status == "active"
