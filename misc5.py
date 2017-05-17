from sys import argv

scriptname, filename = argv

fl = open(filename)
print fl.read()
