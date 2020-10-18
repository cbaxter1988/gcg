from gcg.schemas.network.ip import IPv6Addr, IPv4Addr
from gcg.schemas.network.snmp import BaseSNMPv2, BaseSNMPv3
from marshmallow import Schema, fields


class BaseInterface(Schema):
    link_id = fields.Str(required=True)
    dot1q = fields.Str()
    is_mgmt = fields.Boolean()
    description = fields.Str()
    bandwidth = fields.Str()
    ipv4_addrs = fields.List(fields.Nested(IPv4Addr))
    ipv6_addrs = fields.List(fields.Nested(IPv6Addr))


class BaseNode(Schema):
    hostname = fields.Str(required=True)
    domain = fields.Str(required=True)
    snmpv2 = fields.List(fields.Nested(BaseSNMPv2))
    snmpv3 = fields.List(fields.Nested(BaseSNMPv3))
    interfaces = fields.List(fields.Nested(BaseInterface))
