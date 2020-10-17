import ipaddress

from marshmallow import validate
from marshmallow.exceptions import ValidationError


class IPValidator(validate.Validator):
    def __init__(self):
        pass

    def __call__(self, val):
        try:
            ipaddress.ip_address(val)
        except ValueError as error:
            raise ValidationError(str(error))
