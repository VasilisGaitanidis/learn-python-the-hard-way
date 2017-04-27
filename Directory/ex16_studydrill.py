from sys import argv

script, filename = argv

text = open(filename) # opens file

print text.read() # reads the file

text.close() # closes the file
