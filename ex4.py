# no. of cars
cars = 100
# space in a car
space_in_a_car = 4
# how many drivers?
drivers = 30
# passengers in a car
passengers = 90
# not driven cars
cars_not_driven = cars - drivers
# driven cars
cars_driven = drivers
# capacity of carpool
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car
average_passengers_per_car = passengers / cars_driven

# printing available cars
print "There are", cars, "cars available."
# available drivers
print "There are only", drivers, "drivers available."
# empty cars
print "There will be", cars_not_driven, "empty cars today."
# no. of people can be transported
print "we can transport", carpool_capacity, "people today."
# carpool passengers
print "We have", passengers, "to carpool today."
# passengers per car
print "we need to put about", average_passengers_per_car, "in each car."
