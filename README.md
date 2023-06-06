# Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments
This repository contains all materials related to the talk given by Asaf Aprozper at fwd:cloudsec 2023, titled "Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments". 

## Talk Description
In the world of cloud computing, protecting networks from unauthorized access is critical. This talk delves into a new and less-discussed risk: the use of lookalike private IP ranges. Our investigation revealed that cloud users mistakenly configured Security Groups and VPCs with IP ranges they believed were internal but were actually publicly exposed to US cellular networks and potentially malicious actors.
The presentation will highlight the security risks of lookalike IP addresses in cloud environments and introduce a new community-driven framework called CloudHunting. This framework uses Sigma rules mapped by MITRE ATT&CK to proactively detect such misconfigurations that could lead to threats, including this newly identified one&#8203;``oaicite:{"number":1,"metadata":{"title":"pretalx.com","url":"https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/","text":"Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments \n\n  .ical  \n\n06-13, 11:30–12:10 (US/Pacific), Salon C \n\nIn the world of cloud computing, protecting networks from unauthorized access is critical. While some misconfigurations, such as allowing access from any IP address are widely known, a new and less-discussed risk has emerged: the use of lookalike private IP ranges. In a proactive hunt for possible unknown misconfigurations, it was revealed that cloud users mistakenly configured Security Groups and VPCs with IP ranges they believed were internal, but were actually publicly exposed to US cellular networks and potentially for malicious actors. Such issues blur the lines between customer and cloud vendor responsibility, as customers are responsible for configuring their own networks, but cloud providers can easily assist in mitigating such misconfigurations.\n\nTo evaluate this new misconfiguration and the possible critical risk that is associated with it, we purchased a T-Mobile lookalike private IP address for just a few bucks and implemented it over ProxyChains and NMAP to lookalike the private IP range and scan for open services across AWS ASN. This presentation will highlight the security risks of lookalike IP addresses in cloud environments and introduce a new community-driven framework called CloudHunting, which uses Sigma rules mapped by MITRE ATT&CK to proactively detect such misconfigurations that could lead to threats, including this newly identified one","pub_date":null}}``&#8203;.

## Repository Contents
This repository will contain:
- The presentation slides
- Python script to scan IP ranges and "unmaske" such one's that accessible from proxy IP address only
- Splunk Hunting rules after the creation\modification of security groups that contains lookalike IP ranges


Please note that this repository is for educational purposes only and should be used responsibly.

## References
- [Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments (fwd:cloudsec 2023)](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)

## Authors
**Asaf Aprozper (3pun0x)** - *Creator* - [Twitter](https://twitter.com/3pun0x) - [LinkedIn](https://www.linkedin.com/in/asafaprozper) 

## Contributing
Pull requests and forks are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
