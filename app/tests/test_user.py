import pytest
from app.models import User
from faker import Faker

fake = Faker()

@pytest.fixture
def new_user():
    user = User(username=fake.user_name())
    user.set_password(fake.password())
    return user

def test_new_user(new_user):
    assert new_user.username is not None
    assert new_user.password_hash is not None

def test_user_password(new_user):
    password = fake.password()
    new_user.set_password(password)
    assert new_user.check_password(password) is True
