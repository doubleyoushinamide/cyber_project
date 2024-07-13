#!/bin/bash

: << NOTE
This is a simple script to gather info about users
on the same network as you.
There are more you can add to this but 
this is just the basics.

this program will later be called by a python file
NOTE

# 1. Get list of all IP addresses on the same network as you are
ips=$(sudo arp-scan --localnet | grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}')

# 2. Get list of all MAC addresses corresponding to the IP addresses
mac_addr=$(sudo arp-scan --localnet | grep -o -E '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}')

# 3. Display the list of IP addresses and MAC addresses
echo "IP addresses and MAC addresses on the network:"
# 4. Splitting results into arrays using a loop
ip_array=()
mac_array=()

# I would have used `readarray` if this script was run on a linux/Ubuntu machine
# Instead, I will split ips and macs into seperate arrays and join them using a loop

# 5. Split IP addresses into array
while IFS= read -r line; do
    ip_array+=("$line")
done <<< "$ips"

# Split MAC addresses into array
while IFS= read -r line; do
    mac_array+=("$line")
done <<< "$mac_addr"

# iterating through the arrays and join the IP and MAC addresses side by side
for (( i=0; i<${#ip_array[@]}; i++ )); do
    echo "${ip_array[i]}   ${mac_array[i]}"
done