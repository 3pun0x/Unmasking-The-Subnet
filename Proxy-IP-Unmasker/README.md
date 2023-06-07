# Proxy IP Unmasker

Proxy IP Unmasker is a Python script that leveraging proxing capabilities and performs multiprocessing port scanning on the desired range of IP addresses.
The goal is to identify IP addresses that are only accessible through a specific proxy\IP ranges. This can be particularly useful for unmasking the hidden services or systems which are not reachable via the public internet.

```bash
    ________     __  __                           __            
   /  _/ __ \   / / / /___  ____ ___  ____ ______/ /_____  _____
   / // /_/ /  / / / / __ \/ __ `__ \/ __ `/ ___/ //_/ _ \/ ___/
 _/ // ____/  / /_/ / / / / / / / / / /_/ (__  ) ,< /  __/ /    
/___/_/       \____/_/ /_/_/ /_/ /_/\__,_/____/_/|_|\___/_/     

https://github.com/3pun0x/Unmasking-The-Subnet                                                                
```


## Prerequisites
This script is written in Python and uses several libraries that need to be installed. These libraries include socks, multiprocessing, tqdm, and netaddr. You can install these using requirements.txt:
1. Python 3.6 or above
2. SOCKS5 Proxy server with username and password


## Getting Started
```bash
git clone <repo>
pip install -r requirements.txt
```


## Configuration
To run the script, you need to provide your SOCKS5 proxy settings. Open the script in a text editor and replace the placeholders with your information:
```bash
username = 'your_username'
password = 'your_password'
proxy_server = 'your_proxy_server'
proxy_port = 'your_proxy_port'
```


## Usage
Run the script using Python:
```bash
python ip_unmasker.py
```
When prompted, enter the IP range and port that you want to scan:
```bash
Enter the IP range: x.x.x.x/x
Enter the port: 80
```


## Results
The script will print out any IP addresses that are accessible via the proxy but not via the public internet. It will also display a progress bar indicating the progress of the scan and will print the total time taken for the scan once it's completed.

![](DOCS/scanner_gif.gif)

## References
- [Unmasking the Subnet: Lookalike IP Ranges in Cloud Environments (fwd:cloudsec 2023)](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)

## Contributing
Pull requests and forks are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
**Asaf Aprozper (3pun0x)** - *Creator* - [Twitter](https://twitter.com/3pun0x) - [LinkedIn](https://www.linkedin.com/in/asafaprozper) 

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
