from sys import argv # imports argv

script, filename = argv # sets the argv that will be readed from the cmd

txt = open(filename) # opens the filename we set before from the command line

print "Here's your file %r:" % filename
print txt.read() # reads the txt parametr and prints

txt.close() # closes the file
print "You closed your file."

'''
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
'''
