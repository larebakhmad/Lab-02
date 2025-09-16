#this program will open auth.log and prints each line.
with open("auth.log", "r") as file:
    for line in file:
        print(line.strip())
#now we are gonna use the regex r"\d+\.\d+\.\d+\.\d+" to find all the IP addresses in the auth.log file.
#creating a list (similar to array in java) to store the IP addresses.
import re
ips = []
pattern = r"\d+\.\d+\.\d+\.\d+"
with open("auth.log", "r") as file:
    for line in file:
        found_ips = re.findall(pattern, line)
        ips.extend(found_ips)  # Add found IPs to the list
print(ips)
"""
r"\d+\.\d+\.\d+\.\d+" matches IPv4 addresses.
\d+ matches one or more digits, \. matches a literal dot.
"""
