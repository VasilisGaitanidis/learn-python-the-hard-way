numbers = []

def while_function(start, stop, step):
    i = start
    while i < stop:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i

def for_function(start, stop, step):
    for i in range(start, stop, step):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i

starting_number = int(raw_input("Enter the starting number: \n>")) # needs first to be parsed to integer
last_number = int(raw_input("Enter the last number: \n>"))
step_number = int(raw_input("Enter the step number: \n>"))

# while_function(starting_number, last_number, step_number)
for_function(starting_number, last_number, step_number)


print "The numbers: "
for num in numbers:
    print num
