import copy
import json
import unittest

from gcg.schemas import (
    IPv4Addr
)
from marshmallow.exceptions import ValidationError
from test.vars import data_ipv4_addr_netmask, data_ipv4_addr_cidr


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


if __name__ == '__main__':
    unittest.main()
