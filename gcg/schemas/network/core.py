from marshmallow import Schema, fields
from gcg.schemas.validators import IPValidator
from marshmallow.validate import Length, Range


class IPv6Addr(Schema):
    ipv6_address = fields.Str()
    eui_64 = fields.Str()
    link_local = fields.Str()
    anycast = fields.Str()


class IPv4Addr(Schema):
    address = fields.Str(required=True, validate=IPValidator())
    netmask = fields.Str(validate=IPValidator())
    cidr = fields.Int(validate=Range(1, 32))
