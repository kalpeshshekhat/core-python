name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cms = height * 2.54
weight = 180 # lbs
weight_kgs = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
office_no = 'A'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %E cms tall." % height_cms
print "He's %d pounds heavy." % weight
print "He's %E kgs heavy." % weight_kgs
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "His office no. is %s." % office_no

# this line is tricky, try to get it exactly right
print "If  I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
