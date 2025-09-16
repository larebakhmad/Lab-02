#This program write the uniuqe IPs to a new file unique_ips.txt, one per line.
import re
ips = []
pattern = r"\d+\.\d+\.\d+\.\d+"
with open("auth.log", "r") as file:
    for line in file:
        found_ips = re.findall(pattern, line)
        ips.extend(found_ips)
unique_ips = set(ips)
with open("unique_ips.txt", "w") as outfile:
    for ip in unique_ips:
        outfile.write(ip + "\n")
"""
r"\d+\.\d+\.\d+\.\d+" matches IPv4 addresses.
\d+ matches one or more digits, \. matches a literal dot.
we convert the list to a set to remove duplicates and write each unique IP to unique_ips.txt, one per line.
"""