from wtforms import ValidationError
from ipaddress import ip_address

class ValidationUtils:
    @staticmethod
    def validate_ip(ip):
        try:
            ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_positive(value):
        if value <= 0:
            raise ValidationError("Value must be positive.")
