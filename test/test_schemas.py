import copy
import json
import unittest

from gcg.schemas import (
    IPv4Addr, IPv6Addr
)
from marshmallow.exceptions import ValidationError
from test.vars import (
    data_ipv4_addr_netmask,
    data_ipv4_addr_cidr,
    data_ipv6_addr,
    data_ipv6_eui_64,
    data_ipv6_link_local,
    data_ipv6_anycast

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


if __name__ == '__main__':
    unittest.main()
