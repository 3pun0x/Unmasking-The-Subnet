import socket
import socks
import time
from tqdm import tqdm
from netaddr import IPNetwork

# Your SOCKS5 proxy settings
proxy_server = 'proxy_server_ip'
proxy_port = 'proxy_port'
username = 'your_username'
password = 'your_password'


# Function to check if a port is open
def is_port_open(ip_to_scan, port_to_scan, proxy=False):
    sock = socks.socksocket() if proxy else socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip_to_scan, port_to_scan))
        sock.close()
        return True
    except socket.error:
        return False


if __name__ == '__main__':
    print("""
       __  __                           __   _                ________            _____       __               __ 
      / / / /___  ____ ___  ____ ______/ /__(_)___  ____ _   /_  __/ /_  ___     / ___/__  __/ /_  ____  ___  / /_
     / / / / __ \/ __ `__ \/ __ `/ ___/ //_/ / __ \/ __ `/    / / / __ \/ _ \    \__ \/ / / / __ \/ __ \/ _ \/ __/
    / /_/ / / / / / / / / / /_/ (__  ) ,< / / / / / /_/ /    / / / / / /  __/   ___/ / /_/ / /_/ / / / /  __/ /_  
    \____/_/ /_/_/ /_/ /_/\__,_/____/_/|_/_/_/ /_/\__, /    /_/ /_/ /_/\___/   /____/\__,_/_.___/_/ /_/\___/\__/  
                                                 /____/                                                                                            
    """)
    # Set up the proxy
    socks.set_default_proxy(socks.SOCKS5, proxy_server, int(proxy_port), username=username, password=password)

    # IP Range and port to be checked
    ip_range = input("Enter the IP range: ")
    port = int(input("Enter the port: "))  # Convert to int for use with socket

    # Record start time
    start_time = time.time()

    # Calculate total IPs based on the subnet
    subnet_mask = int(ip_range.split('/')[-1])
    total_ips = 2 ** (32 - subnet_mask)

    # Display a progress bar while iterating the IPs
    for ip in tqdm(IPNetwork(ip_range), total=total_ips):
        ip = str(ip)
        result_proxy = is_port_open(ip, port, proxy=True)
        result_direct = is_port_open(ip, port, proxy=False)

        if result_proxy and not result_direct:
            print(f"\nIP {ip} is accessible via proxy but not directly.")

    # Calculate and print total time taken
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal time taken: {total_time} seconds")
