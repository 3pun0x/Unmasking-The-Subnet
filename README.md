# Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments
This repository contains all materials associated with the talk "Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments" presented by Asaf Aprozper at [fwd:cloudsec 2023](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/).

```bash
   __  __                           __   _                ________            _____       __               __ 
  / / / /___  ____ ___  ____ ______/ /__(_)___  ____ _   /_  __/ /_  ___     / ___/__  __/ /_  ____  ___  / /_
 / / / / __ \/ __ `__ \/ __ `/ ___/ //_/ / __ \/ __ `/    / / / __ \/ _ \    \__ \/ / / / __ \/ __ \/ _ \/ __/
/ /_/ / / / / / / / / / /_/ (__  ) ,< / / / / / /_/ /    / / / / / /  __/   ___/ / /_/ / /_/ / / / /  __/ /_  
\____/_/ /_/_/ /_/ /_/\__,_/____/_/|_/_/_/ /_/\__, /    /_/ /_/ /_/\___/   /____/\__,_/_.___/_/ /_/\___/\__/  
                                             /____/                                                                                            
```

## About the Talk
In the evolving landscape of cloud computing, safeguarding networks from unauthorized access remains crucial. This talk explores a less-discussed risk factor – the use of lookalike private IP ranges. The discussion unfolds our investigation that revealed cloud users' erroneous configuration of Security Groups and VPCs with IP ranges, which they presumed to be internal but were, in fact, publicly exposed to US cellular networks and potentially to malicious actors. The talk not only highlights the security risks associated with lookalike IP addresses in cloud environments but also offers practical hunting rules to mitigate such misconfigurations.

## Repository Contents
- [Proxy IP Unmasker/](https://github.com/3pun0x/Unmasking-The-Subnet/tree/main/Proxy-IP-Unmasker): Python script that scans IPv4 ranges and "unmasks" those only accessible from proxy IP addresses.
- [SG Unmasker/](https://github.com/3pun0x/Unmasking-The-Subnet/blob/main/SG-Unmasker/README.MD): Python script that scans your AWS security groups under a sepcific regsion after misconfigured ingress rules with lookalike private IP ranges
- [Rules/](https://github.com/3pun0x/Unmasking-The-Subnet/tree/main/rules): SIEM Hunting rules triggered by the creation/modification of security groups\FW Rules contains ingress lookalike internal IP ranges of AT&T and T-Mobile.
- `Presentation/`: The slide deck from the talk.

Please use this repository responsibly, as it is intended for educational purposes only.

## References

- [Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments (fwd:cloudsec 2023)](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)

## About the Author

**Asaf Aprozper (3pun0x)** - *Creator* - [Twitter](https://twitter.com/3pun0x) - [LinkedIn](https://www.linkedin.com/in/asafaprozper) 

## Contributing

Contributions are more than welcome! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue first to discuss what you would like to modify.

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
