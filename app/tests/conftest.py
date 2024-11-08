import pytest
from app import create_app, db
from app.models import User, Device
from faker import Faker

fake = Faker()

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("testing")
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope="module")
def init_database():
    db.create_all()

    user = User(username=fake.user_name())
    user.set_password(fake.password())
    db.session.add(user)

    device = Device(
        name=fake.name(),
        location=fake.address(),
        ip_address=fake.ipv4(),
        status="active"
    )
    db.session.add(device)
    db.session.commit()

    yield db

    db.drop_all()
