import ipaddress
import re

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


class IPv6Validator(validate.Validator):
    def __init__(self):
        pass

    def __call__(self, val):
        try:

            if str(val).find("/") > 1:
                i = str(val).index("/")
                val = val[:i]

            ipaddress.ip_address(val)

        except ValueError as error:
            raise ValidationError(str(error))


class IPv6EUI64Validator(validate.Validator):
    def __init__(self):
        pass

    def __call__(self, val):
        pattern = re.compile(".*(/64)", re.I)

        if not pattern.match(val):
            raise ValidationError("Invalid eui-64 address")


class IPv6LinkLocalValidator(validate.Validator):
    def __init__(self):
        pass

    def __call__(self, val):
        pattern = re.compile("(FE80).*", re.I)

        if not pattern.match(val):
            raise ValidationError("Invalid link-local address")
