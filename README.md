# cyber_project

cybersecurity projects codes with python

## Project 1

# Network IP Address Printer and Formatter

## Bash Script (`capture_users.sh`)

This Bash script gathers information about IP addresses on the same network and is intended to be called by a Python script for enhanced formatting.

### Dependencies

- Requires `arp-scan` from `sudo apt-get install arp-scan` on linux or `brew install arp-scan` on Mac.

## Python Script (`format_network_ips.py`)

This Python script enhances the output of the Bash script by formatting the list of IP addresses in a structured manner.

### Dependencies

- Requires `subprocess` and `re` Python modules.
