#this program reads the file.txt as line by line
with open('sample.txt' , 'r') as f:
    for line in f:
        print(line)
"""
this code input the blank line after every lane that is already written in
the text file.
so print statemtent adds a newline and file line already has one.
"""