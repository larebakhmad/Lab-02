import re
#This program reads the regex to match the words instead of numbers
pattern = r"\b[a-zA-Z]+\b"
text = "Order 123 was placed on 2023-05-01."
print(re.findall(pattern, text))

"""
r"\b[a-zA-Z]+\b" matches whole words consisting of letters only.
\b asserts a word boundary, [a-zA-Z]+ matches one or more letters (both uppercase and lowercase).
"""
