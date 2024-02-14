#!/bin/bash

until openvpn /etc/openvpn/systemxc/key.ovpn; do
    echo "OpenVPN crashed with error $?. Restarting..." >&2
    sleep 1
done
