# Genesis Configuration Generator

This tool is used to generate configurations for numerous types of devices and services. The goal of this service is to
provide users the ability to quickly define their own configuration definition to later be used for rapid and consistent
configuration generation. This tool also supports the ability to store configurations to an AWS S3 cloud. 


Both the docker-cli and API utilize JSON models for input.  There are required model keys for each configuration request type. 

### Public API 
This service is deployed to Amazon AWS and is available for public consumption. Use the following endpoint to generate
configurations of your own. 

- URL - lb.cbaxterjr.com/api/v1/gcg

Use to validate if service is alive.
```bash
curl --location --request GET 'http://lb.cbaxterjr.com:80/health'
```

Generates a Basic Cisco IOS Config
```bash
curl --location --request POST 'http://lb.cbaxterjr.com:80/api/v1/gcg?return_type=text&name=R1-CORE&store_aws=false&lab_name=NOC_A_LAB&template_type=ios_base_node' \
--header 'Content-Type: application/json' \
--data-raw '{
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
}'
```

### Docker Compose 
```yaml
version: '3.1'

services:
  app:
    image: cbaxter1988/gcg
    ports:
      - 5000:5000
    environment:
      - APP_PORT=5000
      - AWS_ACCESS_KEY=YOUR_AWS_KEY
      - AWS_SECRET_KEY=YOUR_AWS_SECRET
      - TEMP_FOLDER=/var/tmp
      - DEBUG=false
```

### local installation 
```bash
git clone https://github.com/cbaxter1988/gcg.git
cd gcg 

python3 setup.py sdist

pip install dist/lcg-1.tar.gz
```


### CLI Usage 
```bash
python -m gcg [-h]
```

Help Text:
```text
usage: gcg [-h] [--run] [--json JSON]
                   [--template_type {ios_base_node,ios_te_tunnels,ios_bgp_policy,ios_bgp_session,ios_explicit_path,ios_vpls,ios_evpn,xr_base_config,linux_netplan_base}]
                   [--store_aws] [--store_local]
                   [--aws_access_key AWS_ACCESS_KEY]
                   [--aws_secret_key AWS_SECRET_KEY]
                   [--save_location SAVE_LOCATION] [--config_name CONFIG_NAME]

Genesis Configuration Generator

optional arguments:
  -h, --help            show this help message and exit
  --run                 Runs Development HTTP server used to deploy Genesis
                        Configuration Generator

Commands for running the GCG CLI tool:
  --json JSON           Specify the JSON file you would like to generate.
  --template_type {ios_base_node,ios_te_tunnels,ios_bgp_policy,ios_bgp_session,ios_explicit_path,ios_vpls,ios_evpn,xr_base_config,linux_netplan_base}
  --store_aws           Flag to store rendered config to AWS
  --store_local         Flag to store rendered config to local file system
  --aws_access_key AWS_ACCESS_KEY
                        Access Key used for AWS Boto3 session
  --aws_secret_key AWS_SECRET_KEY
                        Secret Key used for AWS Boto3 session
  --save_location SAVE_LOCATION
                        Specify location to save the generated config
  --config_name CONFIG_NAME
                        Specify the name of the Generated configuration .txt
                        file

Process finished with exit code 0
```

Run Internal Server
```bash
python -m gcg --run 
```

