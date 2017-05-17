# Animal is-a object
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
      ## ??
      super(Employee, self).__init__(name)
      ## ??
      self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## is-a
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()
