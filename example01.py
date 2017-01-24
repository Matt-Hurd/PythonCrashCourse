'''
Classes are types of objects. These objects can hold other objects, such as variables.
Classes can also have special functions that are unique to only themselves.
When these functions are run, they act on the object that calls them.
'''
class Car():
    def __init__(self, color, make, model): #Whenever an object of a certain class is made (see line 17), it runs __init__
        self.color = color #Set the object's color to be equal to the passed in color
        self.make = make
        self.model = model
        self.state = 'stopped'

    def start(self):
        self.state = 'started'
        print('vroom')

my_car = Car("Red", "Toyota", "Corolla") #Create a car object
print(my_car.make) #Print out the make of the car, which is a variable that belongs to the object.
my_car.start() #Call my_car's start function, which modifies my_car
#'vroom' is printed by the my_car.start() function