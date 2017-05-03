ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # creates a list from the ten_things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # removes and returns item at index
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff) # len function return the number of items inside the list

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # prints the 2nd string inside stuff
print stuff[-1]
print stuff.pop() # pop function removes and returns the item at index (last string in the stuff)
print ' '.join(stuff) # joins the strings inside the list with a space (' ')
print '#'.join(stuff[3:5]) # joins the strings at positions 3-4 with a #
