import socket
import socks
import time
from multiprocessing import Pool
from netaddr import IPNetwork
import tqdm


# ASCII Art
ascii_art = ("""
    ________     __  __                           __            
   /  _/ __ \   / / / /___  ____ ___  ____ ______/ /_____  _____
   / // /_/ /  / / / / __ \/ __ `__ \/ __ `/ ___/ //_/ _ \/ ___/
 _/ // ____/  / /_/ / / / / / / / / / /_/ (__  ) ,< /  __/ /    
/___/_/       \____/_/ /_/_/ /_/ /_/\__,_/____/_/|_|\___/_/     

https://github.com/3pun0x/Unmasking-The-Subnet
""")


# Your SOCKS5 proxy settings
proxy_server = 'proxy_server_ip'
proxy_port = 'proxy_port'
username = 'your_username'
password = 'your_password'


def set_proxy():
    socks.set_default_proxy(socks.SOCKS5, proxy_server, int(proxy_port), username=username, password=password)


# Function to check if a port is open
def scan_ip(args):
    ip, port = args
    result_proxy = is_port_open(ip, port, proxy=True)
    result_direct = is_port_open(ip, port, proxy=False)
    return ip, result_proxy, result_direct


def is_port_open(ip, port, proxy=False):
    sock = socks.socksocket() if proxy else socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((ip, port))
        sock.close()
        return True
    except socket.error:
        return False


def ip_unmasker():
    print(ascii_art)
    set_proxy()

    # IP Range and port to be checked
    ip_range = input("Enter the IP range: ")
    port = int(input("Enter the port: "))  # Convert to int for use with socket

    # Record start time
    start_time = time.time()

    # Calculate total IPs based on the subnet
    subnet_mask = int(ip_range.split('/')[-1])
    total_ips = 2 ** (32 - subnet_mask)

    # Create a Pool of subprocesses
    with Pool() as pool:
        # Prepare the arguments for each process
        args = [(str(ip), port) for ip in IPNetwork(ip_range)]

        # Iterate over each IP in the range and start a new process for each one
        for ip, result_proxy, result_direct in tqdm.tqdm(pool.imap_unordered(scan_ip, args), total=total_ips):
            if result_proxy and not result_direct:
                print(f"\nIP {ip} is accessible via proxy but not directly.")

    # Calculate and print total time taken
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal time taken: {total_time} seconds")


if __name__ == '__main__':
    ip_unmasker()
