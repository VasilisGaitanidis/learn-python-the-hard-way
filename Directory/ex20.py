from sys import argv

script, input_file = argv

def print_all(f):   # prints the file after reading it
    print f.read()

def rewind(f):
    f.seek(0) # moving to the start of the file

def print_a_line(line_count, f): # prints only the line_count of the file
    print line_count, f.readline() # readline() reading a line from the file

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
