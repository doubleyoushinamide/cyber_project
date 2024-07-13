#!/usr/bin/env python3
import subprocess
import re

def get_network_ips():
    # Run the bash script and capture its output
    result = subprocess.run(['bash', 'capture_users.sh'], capture_output=True, text=True)
    
    # Extract the IP addresses from the output using regex
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', result.stdout)
    
    # Print formatted output
    print("Formatted list of IP addresses:")
    for ip in ips:
        print(f"- {ip}")

if __name__ == "__main__":
    get_network_ips()
