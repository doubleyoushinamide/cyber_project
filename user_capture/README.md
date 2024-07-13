## Project 1

# Network IP and MAC Address Printer and Formatter (LAN SCANNER)

## Bash Script (`capture_users.sh`)

This Bash script gathers information about IP addresses on the same network and is intended to be called by a Python script for enhanced formatting.

### Usage

1. **Functionality:**
   - Retrieves a list of IP addresses using `arp-scan`.
   - Uses `grep` with a regular expression to filter and capture IP addresses from the output.

2. **Execution:**
   - When executed, it displays the list of IP addresses detected on the local network.

### Notes

- This script provides basic functionality to identify active IP addresses on the network.
- Designed as a foundation for more advanced network analysis and monitoring tasks.

---

## Python Script (`format_network_ips.py`)

This Python script enhances the output of the Bash script by formatting the list of IP addresses in a structured manner.

### Dependencies

- Requires `subprocess` and `re` Python modules.

### Usage

1. **Functionality:**
   - Executes the Bash script (`capture_users.sh`) to fetch IP addresses.
   - Uses regex (`re.findall`) to extract IP addresses from the Bash script's output.
   - Prints each IP address in a formatted list.

2. **Execution:**
   - Invokes the Bash script using `subprocess.run` and captures its output.
   - Processes the output to extract and display IP addresses in a user-friendly format.

### Example Output

- Displays a formatted list of IP addresses detected on the network.

### Integration

- Intended to be integrated into larger network monitoring or analysis applications.
- Provides a seamless connection between Bash and Python for network information retrieval and processing.

---

## Conclusion

This documentation outlines a simple yet effective solution for discovering and formatting IP addresses of users on a local network. The combination of Bash for initial data gathering and Python for enhanced output formatting ensures clarity and ease of use in network administration tasks.
