import re
#This program reads the regex to match the words instead of numbers
#Adding another IP address into the string and check if both are found.
pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30 and 10.0.0.5"
print(re.findall(pattern, text))
"""
r"\d+\.\d+\.\d+\.\d+" matches IPv4 addresses.
\d+ matches one or more digits, \. matches a literal dot.
we put another IP address into the string and check if both are found.
"""
