# import argv from sys module
from sys import argv
# unpacking arguements from argv
script, filename = argv
# print some instructions
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# taking input
raw_input("?")
# making target an object of open file function with write mode
print "Opening the file..."
target = open(filename, 'w')
# wiping a file taken through target object
print "Truncating the file. Goodbye!"
target.truncate()
# taking three lines from user
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# writing those lines to file attached to target object
target.write(line1 line2 line3)
# close file by using target object
print "And finally, we close it."
target.close()
