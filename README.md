# Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments
This repository contains all materials associated with the talk "Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments" presented by Asaf Aprozper at [fwd:cloudsec 2023](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/).

## About the Talk
In the evolving landscape of cloud computing, safeguarding networks from unauthorized access remains crucial. This talk explores a less-discussed risk factor – the use of lookalike private IP ranges. The discussion unfolds our investigation that revealed cloud users' erroneous configuration of Security Groups and VPCs with IP ranges, which they presumed to be internal but were, in fact, publicly exposed to US cellular networks and potentially to malicious actors. The talk not only highlights the security risks associated with lookalike IP addresses in cloud environments but also offers practical hunting rules to mitigate such misconfigurations.

## Repository Contents
- `presentation/`: The slide deck from the talk.
- `Proxy IP Unmasker/`: Python script that scans IP ranges and "unmasks" those only accessible from proxy IP addresses.
- `rules/`: Splunk Hunting rules triggered by the creation/modification of security groups containing lookalike IP ranges.

Please use this repository responsibly, as it is intended for educational purposes only.

## References

- [Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments (fwd:cloudsec 2023)](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)

## About the Author

**Asaf Aprozper (3pun0x)** is the creator of this repository and the presenter of the talk. You can reach out to him on [Twitter](https://twitter.com/3pun0x) or connect with him on [LinkedIn](https://www.linkedin.com/in/asafaprozper). 

## Contributing

Contributions are more than welcome! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue first to discuss what you would like to modify.

## License

This repository is licensed under the Apache License 2.0. [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
