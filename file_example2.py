#this program finds all occurrences of the word "cat" in a given text.
import re
pattern = r"cat"
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)

#this program finds all the numbers in a given text.
import re

pattern = r"\d+"
text = "Order 123 was placed on 2023-05-01."
print(re.findall(pattern, text))

#This program reads the regex to match the words instead of numbers
import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30"
print(re.findall(pattern, text))
