# storing integer variable embedded string into variable
x = "There are %d types of people." % 10
# storing string into variable
binary = "binary"
# storing another string into variable
do_not = "don't"
# storing string variable embedded string into variable
y = "Those who know %s and those who %s." % (binary, do_not)

# printing value of variable x
print x
# printing value of variable y
print y

# printing string & value of variale x
print "I said: %r." % x
# printing string & value of variable y
print "I also said: %s." % y

# assigning string value to variable
hilarious = False
# assigning string to variable
joke_evaluation = "Isn't that joke so funny?! %r"

# printing variable value
print joke_evaluation % hilarious

# assigning string to w & e
w = "This is the left side of..."
e = "a string with a right side."

# printing w + e
print w + e
