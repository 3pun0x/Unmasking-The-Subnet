# SG Unmasker

SG Unmasker is a Python tool that checks AWS Security Groups in a specific region that misconfigured with inbound lookalike private IP ranges.

## Features
- Fetches all Security Groups in a specified AWS region
- Checks inbound rules for certain IP ranges, excluding valid Private IPv4 Class B ranges
- Printing when it identifies a Security Group that allows traffic from the specified IP ranges

## Prerequisites
- Python 3.6+
- Boto3

## Installation
1. Clone this repository
2. Navigate to the cloned repository
3. Run the script

## Usage
Run the tool with Python:
```bash
python sg_unmasker.py
```
When prompted, enter the region you would like to scan after misconfigured security groups with lookalike private IP ranges
```bash
Enter the region to search in: us-east-1
```

## Results
The script will print out any security group that contains lookalike private ip ranges.

## References
- [Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments (fwd:cloudsec 2023)](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)

## Contributing
Pull requests and forks are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
**Asaf Aprozper (3pun0x)** - *Creator* - [Twitter](https://twitter.com/3pun0x) - [LinkedIn](https://www.linkedin.com/in/asafaprozper) 

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
