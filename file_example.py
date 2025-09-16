#this program reads the file.txt as line by line
with open('sample.txt' , 'r') as f:
    for line in f:
        print(line)

#this program reads file.txt as stripping newlines
with open('sample.txt' , 'r') as f:
    for line in f:
        print(line.strip())

#this program writes to the file.txt
with open('output.txt', 'w') as f:
    f.write("This is a new file.\n")
    f.write("It has two lines.\n")