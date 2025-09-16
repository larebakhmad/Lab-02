import re
#this program finds all occurrences of the word "at" in a given text.
pattern = r"at"
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)

"""this program finds all the numbers in a given text.
r is used to indicate a raw string, which tells Python to treat backslashes as literal characters and not as escape characters.
\d+ is a regular expression pattern that matches one or more digits (0-9) in a row.
+ is a quantifier that means "one or more" of the preceding element, which in this case is \d (a digit).
findall is a function from the re module that returns all non-overlapping matches of the pattern in the string as a list of strings.
so it finds all the numbers in the given text and returns them as a list of strings.
and print statement to print the list of numbers found in the text.