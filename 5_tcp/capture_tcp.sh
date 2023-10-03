#!/bin/bash

# Capture tcp on port $1
# Usage: capture_tcp.sh <port>

# When done it should ask if you want to open in wireshark

if [ "$1" == "" ]; then
    echo "Usage: capture_tcp.sh <port>"
    exit 1
fi

if [ $EUID -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

rm -f /tmp/capture.pcap

tcpdump -i any -s 65535 -w /tmp/capture.pcap port $1

