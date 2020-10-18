import unittest

import requests
from test_integration.vars import SERVICE_PORT, SERVICE_URL
from gcg.env import AWS_SECRET_KEY, AWS_ACCESS_KEY

class MyTestCase(unittest.TestCase):
    def test_health_service(self):
        """
        Preforms basic health check on running service instance

        """
        url = f"{SERVICE_URL}:{SERVICE_PORT}/health"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_ios_base_node_text(self):
        """
        Generates a cisco ios configurations, test for text return.

        """
        import requests

        url = f"{SERVICE_URL}:{SERVICE_PORT}/api/v1/gcg?return_type=text&name=R1-CORE&store_aws=false&lab_name=NOC_A_LAB&template_type=ios_base_node"
        payload = """
            {
            "hostname": "R12-CORE",
            "domain": "bits.local",
            "interfaces": [
                {
                    "link_id": "lo0",
                    "description": "MGMT Interface",
                    "ipv4_addrs": [
                        {
                            "address": "10.0.0.1",
                            "netmask": "255.255.255.255"
                        }
                    ]
                },
                {
                    "link_id": "Gi1",
                    "bandwidth": "100",
                    "description": "CSR2",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "network_type": "point-to-point",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.2.4.2",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:2:4::2/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi2",
                    "bandwidth": "50",
                    "description": "CSR3",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "network_type": "point-to-point",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.3.4.2",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:3:4::2/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi3",
                    "bandwidth": "100",
                    "description": "CSR7",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.4.7.1",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:4:7::1/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi4",
                    "bandwidth": "100",
                    "description": "CSR8",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.4.8.1",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:4:8::1/64"
                        }
                    ]
                }
            ]
        }
        """
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': AWS_ACCESS_KEY,
            'x-api-secret': AWS_SECRET_KEY
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertIsInstance(response.text, str)
        self.assertEqual(response.headers['Content-Type'], 'text/plain; charset=utf-8')

    def test_ios_base_node_json(self):
        """
        Generates a cisco ios configurations, test for json return.

        """
        import requests

        url = f"{SERVICE_URL}:{SERVICE_PORT}/api/v1/gcg?return_type=json&name=R1-CORE&store_aws=false&lab_name=NOC_A_LAB&template_type=ios_base_node"
        payload = """
            {
            "hostname": "R12-CORE",
            "domain": "bits.local",
            "interfaces": [
                {
                    "link_id": "lo0",
                    "description": "MGMT Interface",
                    "ipv4_addrs": [
                        {
                            "address": "10.0.0.1",
                            "netmask": "255.255.255.255"
                        }
                    ]
                },
                {
                    "link_id": "Gi1",
                    "bandwidth": "100",
                    "description": "CSR2",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "network_type": "point-to-point",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.2.4.2",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:2:4::2/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi2",
                    "bandwidth": "50",
                    "description": "CSR3",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "network_type": "point-to-point",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.3.4.2",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:3:4::2/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi3",
                    "bandwidth": "100",
                    "description": "CSR7",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.4.7.1",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:4:7::1/64"
                        }
                    ]
                },
                {
                    "link_id": "Gi4",
                    "bandwidth": "100",
                    "description": "CSR8",
                    "mpls": {
                        "ldp": true
                    },
                    "ospf": {
                        "p_id": "1",
                        "area_id": "100",
                        "auth": {
                            "is_null": true
                        }
                    },
                    "ipv4_addrs": [
                        {
                            "address": "10.4.8.1",
                            "netmask": "255.255.255.252"
                        }
                    ],
                    "ipv6_addrs": [
                        {
                            "ipv6_address": "2001:4:8::1/64"
                        }
                    ]
                }
            ]
        }
        """
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'AKIA6MRXVMB5NBSTYHO2',
            'x-api-secret': '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'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')


if __name__ == '__main__':
    unittest.main()
