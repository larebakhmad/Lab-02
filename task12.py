with open('sample.txt','r') as f:
    for i, line in enumerate(f, start=1):
        print(i, ":", line.strip())
#this program reads the file.txt as line by line
"""
this program ready the file and adds line numbers before each line.
so it uses enumerate function to add line numbers.
and strip function to remove the newlines.
and start=1 to start line numbers from 1 instead of 0.
by default it starts from 0.
and print statement to print line numbers and lines.
and colon to separate line numbers and lines.
and space after colon for better readability.
and also it uses with statement to open and close the file automatically.
and 'r' mode to read the file.
and 'sample.txt' is the name of the file to be read.
and i is the variable to store line numbers.
"""