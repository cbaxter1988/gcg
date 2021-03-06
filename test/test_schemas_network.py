import copy
import json
import unittest

from gcg.schemas import (
    IPv4Addr,
    IPv6Addr,
    BaseSNMPv2,
    BaseSNMPv3
)
from gcg.schemas.network.snmp import SNMPV3_MODES, AUTH_ALGS, PRIV_ALGS
from marshmallow.exceptions import ValidationError
from test.vars import (
    data_ipv4_addr_netmask,
    data_ipv4_addr_cidr,
    data_ipv6_addr,
    data_ipv6_eui_64,
    data_ipv6_link_local,
    data_ipv6_anycast,
    data_base_snmpv2,
    data_base_snmpv3_auth_priv,
    data_base_snmpv3_auth_no_priv,
    data_base_snmpv3_no_auth_no_priv

)


class IPV4TestCase(unittest.TestCase):
    def test_case_1(self):
        """
        Creates a new IPV4Addr() schema with netmask

        """
        schema = IPv4Addr()

        data = copy.deepcopy(data_ipv4_addr_netmask)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

        del data['address']

        with self.assertRaises(ValidationError):
            schema.load(data)

    def test_case_2(self):
        """
        Creates a new IPV4Addr() schema with cidr

        """
        schema = IPv4Addr()

        data = copy.deepcopy(data_ipv4_addr_cidr)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_3(self):
        """
        Test for IPv4 validation exceptions

        """
        schema = IPv4Addr()

        data_cidr = copy.deepcopy(data_ipv4_addr_cidr)

        with self.assertRaises(ValidationError):
            """
            Test for bad cidr.
            """
            data = copy.deepcopy(data_cidr)

            data['cidr'] = 34

            schema.load(data)

        with self.assertRaises(ValidationError):
            """
            Test for bad address 
            
            """
            data = copy.deepcopy(data_cidr)

            data['address'] = "260.0.0.0"

            schema.load(data)

        with self.assertRaises(ValidationError):
            """
            Test for bad netmask 

            """
            data = copy.deepcopy(data_cidr)

            data['netmask'] = "260.0.0.0"

            schema.load(data)


class IPV6TestCase(unittest.TestCase):
    def test_case_1(self):
        """
        Creates basic IPv6 address
        """
        schema = IPv6Addr()

        data = copy.deepcopy(data_ipv6_addr)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_2(self):
        """
        Creates basic IPv6 address
        """
        schema = IPv6Addr()

        data = copy.deepcopy(data_ipv6_addr)
        data['ipv6_address'] = '2001:0db8:85a3::8a2e:0370:7334'
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

        with self.assertRaises(ValidationError):
            """
            Tests for bad ipv6_address
            """
            data['ipv6_address'] = "1::1::"
            schema.load(data)

    def test_case_3(self):
        """
        Creates basic IPv6 eui-64
        """
        schema = IPv6Addr()

        data = copy.deepcopy(data_ipv6_eui_64)

        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

        with self.assertRaises(ValidationError):
            """
            Tests for Bad eui-64 address
            """
            data['eui_64'] = "2001:BAE:274F:BAED::/66"
            schema.load(data)

    def test_case_4(self):
        """
        Creates basic IPv6 link-local
        """
        schema = IPv6Addr()

        data = copy.deepcopy(data_ipv6_link_local)

        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

        with self.assertRaises(ValidationError):
            """
            Tests for Bad eui-64 address
            """
            data['link_local'] = "FEC0::C001:37FF:FE6C:0"
            schema.load(data)

    def test_case_5(self):
        """
        Creates basic IPv6 anycast

        """
        schema = IPv6Addr()

        data = copy.deepcopy(data_ipv6_anycast)

        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

        with self.assertRaises(ValidationError):
            """
            Tests for Bad eui-64 address
            """
            data['anycast'] = "FEC0::C001:37FF:FE6C::0"
            schema.load(data)


class BaseSNMPv2TestCase(unittest.TestCase):

    def test_case_1(self):
        """
        Test for basic SNMPv2 config

        """
        schema = BaseSNMPv2()

        data = copy.deepcopy(data_base_snmpv2)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_2(self):
        """
        Test all possible snmpv2 group types

        """
        schema = BaseSNMPv2()

        data = copy.deepcopy(data_base_snmpv2)

        data['group_type'] = "rw"
        self.assertIsInstance(schema.load(data), dict)

        data['group_type'] = "ro"
        self.assertIsInstance(schema.load(data), dict)

        with self.assertRaises(ValidationError):
            data['group_type'] = "bad_type"
            self.assertIsInstance(schema.load(data), dict)

    def test_case_3(self):
        """
        Test for required community key.

        """
        schema = BaseSNMPv2()

        data = copy.deepcopy(data_base_snmpv2)

        del data['community']

        with self.assertRaises(ValidationError):
            schema.load(data)


class BaseSMNPv3TestCase(unittest.TestCase):
    def test_case_1(self):
        """
        Test Basic SNMPv3 AuthPriv validation

        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_auth_priv)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_2(self):
        """
        Test Basic SNMPv3 AuthNoPriv validation

        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_auth_no_priv)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_3(self):
        """
        Test Basic SNMPv3 NoAuthNoPriv validation

        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_no_auth_no_priv)
        json_str = json.dumps(data)

        self.assertIsInstance(schema.load(data), dict)
        self.assertIsInstance(schema.loads(json_str), dict)

    def test_case_4(self):
        """
        Test for SNMPv3 modes
        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_no_auth_no_priv)
        json_str = json.dumps(data)

        for mode in SNMPV3_MODES:
            data['mode'] = mode
            self.assertIsInstance(schema.load(data), dict)

        with self.assertRaises(ValidationError):
            data['mode'] = "bad_mode"
            schema.load(data)

    def test_case_5(self):
        """
        Test for SNMPv3 Auth Algs
        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_auth_priv)

        for auth_alg in AUTH_ALGS:
            data['auth_alg'] = auth_alg
            self.assertIsInstance(schema.load(data), dict)

        with self.assertRaises(ValidationError):
            data['auth_alg'] = "bad_alg"
            schema.load(data)

    def test_case_6(self):
        """
        Test for SNMPv3 Priv Algs
        """
        schema = BaseSNMPv3()

        data = copy.deepcopy(data_base_snmpv3_auth_priv)

        for priv_alg in PRIV_ALGS:
            data['priv_alg'] = priv_alg
            self.assertIsInstance(schema.load(data), dict)

        with self.assertRaises(ValidationError):
            data['priv_alg'] = "bad_alg"
            schema.load(data)


if __name__ == '__main__':
    unittest.main()
