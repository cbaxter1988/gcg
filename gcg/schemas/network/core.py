from gcg.schemas.validators import IPValidator, IPv6Validator, IPv6EUI64Validator, IPv6LinkLocalValidator
from marshmallow import Schema, fields
from marshmallow.validate import Range


class IPv6Addr(Schema):
    ipv6_address = fields.Str(validate=IPv6Validator())
    eui_64 = fields.Str(validate=IPv6EUI64Validator())
    link_local = fields.Str(validate=IPv6LinkLocalValidator())
    anycast = fields.Str(validate=IPv6Validator())


class IPv4Addr(Schema):
    address = fields.Str(required=True, validate=IPValidator())
    netmask = fields.Str(validate=IPValidator())
    cidr = fields.Int(validate=Range(1, 32))
