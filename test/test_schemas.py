import unittest
from test.vars import data_ipv4_addr_cidr, data_ipv4_addr_netmask
from gcg.schemas import (
    IPv4Addr
)


class IPV4TestCase(unittest.TestCase):
    def test_case_1(self):
        """
        Creates a new IPV4Addr() schema
        """
        schema = IPv4Addr()



        results = schema.validate(data_ipv4_addr_cidr)
        self.assertIsInstance(results, dict)




if __name__ == '__main__':
    unittest.main()
