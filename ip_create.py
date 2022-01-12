"""Small script to create test files"""
import ipaddress
import random

net = ipaddress.ip_network("10.0.0.0/8").subnets(new_prefix=24)

networks = [str(n.network_address) for n in net]

# Ordered list of subnets
with open("ordered_ip.txt", "w", encoding="utf-8") as file:
    for net in networks:
        file.write(f"{net}\n")

# Reversed list of subnets
networks.reverse()
with open("reverse_ip.txt", "w", encoding="utf-8") as file:
    for net in networks:
        file.write(f"{net}\n")

# Random list of subnets
random.shuffle(networks)
with open("random_ip.txt", "w", encoding="utf-8") as file:
    for net in networks:
        file.write(f"{net}\n")
