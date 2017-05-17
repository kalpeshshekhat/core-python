# import argv module from sys
from sys import argv
# unpacking argv
script, input_file = argv
# function to print whole file
def print_all(f):
    print f.read()
# function to rewind position to line 0
def rewind(f):
    f.seek(25)
# function to print line no. & a line
def print_a_line(line_count, f):
    print line_count, f.readline(),
# open a file & assign to variable
current_file = open(input_file)
# print messsage
print "First let's print the whole file:\n"
# calling a function
print_all(current_file)
# print message again
print "Now let's rewind, kind of like a tape."
# calling rewind function
rewind(current_file)
# print message
print "Let's print four lines:"
# setting current line position to 1
current_line = 1
# calling function to print a line
print_a_line(current_line, current_file)
# incrementing value of current line by 1
current_line += current_line
# print a message
print_a_line(current_line, current_file)
# incrementing value of current line by 1
current_line = current_line + 1
# calling function to print line no & line of file
print_a_line(current_line, current_file)

current_line = current_line + 2

print_a_line(current_line, current_file)
