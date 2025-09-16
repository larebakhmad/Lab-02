#This prorgam will copies all lines from sample.txt to output.txt
with open('sample.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line)
"""
this program opens sample.txt in read mode and output.txt in write mode.
it reads each line from sample.txt and writes it to output.txt.
it uses with statement to ensure files are properly closed after their suite finishes.
it uses 'r' mode to read the file and 'w' mode to write to the file.
it uses infile and outfile as file objects for reading and writing respectively.
it uses a for loop to iterate through each line in infile and writes it to outfile.
it uses write method to write each line to output file.
it ensures that the content of sample.txt is copied exactly to output.txt, including newlines.
"""