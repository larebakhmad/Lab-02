#this program converts the list to a set, then print each unique IP.
#convert to a set to remove duplicates
import re
ips = []
unique_ips = set(ips)
print("Unique IP addresses:")
pattern = r"\d+\.\d+\.\d+\.\d+"
with open("auth.log", "r") as file:
    for line in file:
        found_ips = re.findall(pattern, line)
        ips.extend(found_ips)
    for ip in set(ips):
        print(ip)
"""
r"\d+\.\d+\.\d+\.\d+" matches IPv4 addresses.
\d+ matches one or more digits, \. matches a literal dot.
and we convert the list to a set to remove duplicates.
"""
