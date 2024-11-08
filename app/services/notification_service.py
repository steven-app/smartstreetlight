from flask_mail import Message
from app import mail

class NotificationService:
    @staticmethod
    def send_email(subject, recipients, body):
        msg = Message(subject, recipients=recipients, body=body)
        mail.send(msg)
