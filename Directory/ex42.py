## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def print_name(self):
        print "The dog's name is", self.name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    def print_name(self):
        print "The cat's name is ", self.name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def print_info(self):
        print "This person's name is", self.name

        if self.pet == None:
            print "And he/she hasn't a pet."
        else:
            print "And his/her pet is a", self.pet.name


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee inherits from Person the name variable
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
rover.print_name()
## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet which is-a Cat
# mary.pet = satan
mary.print_info()

## frank is-a Employee named Frank with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet which is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
