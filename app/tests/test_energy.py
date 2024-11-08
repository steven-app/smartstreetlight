import pytest
from app.models import Energy
from datetime import datetime

@pytest.fixture
def new_energy():
    return Energy(consumption=123.45, timestamp=datetime.now())

def test_new_energy(new_energy):
    assert new_energy.consumption == 123.45
    assert new_energy.timestamp is not None
