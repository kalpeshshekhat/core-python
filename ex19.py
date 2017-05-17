# defining a function taking 2 args & printing values of it
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
# calling a function with 2 values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# assigning values to 2 variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# calling function by passing 2 variables as args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# calling function with 2 math operations as args
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# calling function with 2 var+value as args
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
