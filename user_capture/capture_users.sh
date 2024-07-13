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

# 2. Display the list of IP addresses
echo "IP addresses on the network:"
echo "$ips"