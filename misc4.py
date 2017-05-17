
flname = raw_input("Enter filename to read : ")
# open file & assign it to variable
txt = open(flname)
# print previously opened file by using variable & read function
print "Here's your file %r" % flname
print txt.read()

txt.close()
