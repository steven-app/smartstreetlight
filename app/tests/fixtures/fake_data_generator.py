from faker import Faker
from app.models import User, Device

fake = Faker()

def generate_fake_user():
    user = User(username=fake.user_name())
    user.set_password(fake.password())
    return user

def generate_fake_device():
    device = Device(
        name=fake.name(),
        location=fake.address(),
        ip_address=fake.ipv4(),
        status="active"
    )
    return device
