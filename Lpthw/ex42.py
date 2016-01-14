# --coding: utf-8 --

## Animal is-a object
class Animal(object):
    pass
## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ##Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ##Person has-a name
        self.name = name
        print 'a'

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person:
class Employee(Person):
    
    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a sallary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
# mary = Person("Mary")

## mary ha-a pet named Satan
# mary.pet = satan

## frank is-a Empoyee
frank = Employee("Frank", 12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

