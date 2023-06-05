# Proxy IP Unmasker

Proxy IP Unmasker is a Python script that performs port scanning on a range of IP addresses. The goal is to identify IP addresses that are only accessible through a specific proxy. This can be particularly useful for unmasking the hidden services or systems which are not directly reachable.

```bash
   __  __                           __   _                ________            _____       __               __ 
  / / / /___  ____ ___  ____ ______/ /__(_)___  ____ _   /_  __/ /_  ___     / ___/__  __/ /_  ____  ___  / /_
 / / / / __ \/ __ `__ \/ __ `/ ___/ //_/ / __ \/ __ `/    / / / __ \/ _ \    \__ \/ / / / __ \/ __ \/ _ \/ __/
/ /_/ / / / / / / / / / /_/ (__  ) ,< / / / / / /_/ /    / / / / / /  __/   ___/ / /_/ / /_/ / / / /  __/ /_  
\____/_/ /_/_/ /_/ /_/\__,_/____/_/|_/_/_/ /_/\__, /    /_/ /_/ /_/\___/   /____/\__,_/_.___/_/ /_/\___/\__/  
                                             /____/                                                                                            
```

# Getting Started
These instructions will guide you on how to execute the Proxy IP Unmasker script.


## Prerequisites
This script is written in Python and uses several libraries that need to be installed. These libraries include socks, multiprocessing, tqdm, and netaddr. You can install these using requirements.txt:
```bash
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
python proxy_ip_unmasker.py
```
When prompted, enter the IP range and port that you want to scan:
```bash
Enter the IP range: x.x.x.x/x
Enter the port: 80
```


## Results
The script will print out any IP addresses that are accessible via the proxy but not directly. It will also display a progress bar indicating the progress of the scan and will print the total time taken for the scan once it's completed.

## References
- [fwd:cloudsec 2023](https://pretalx.com/fwd-cloudsec-2023/talk/XDU89P/)


## Authors
**Asaf Aprozper (3pun0x)** - *Creator* - [Twitter](https://twitter.com/3pun0x) - [LinkedIn](https://www.linkedin.com/in/asafaprozper) 
