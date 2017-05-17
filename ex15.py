# import argv functionality from sys module
from sys import argv

# packing arguements into argv
script, filename = argv

# open file & assign it to variable
txt = open(filename)
# print previously opened file by using variable & read function
print "Here's your file %r:" % filename
print txt.read()
txt.close()
# asking for filename & storing filename into variable
print "Type the filename again:"
file_again = raw_input("> ")
# open file & assign it to variable
txt_again = open(file_again)
# print previously opened file by using variable & read function
print txt_again.read()
txt_again.close()
