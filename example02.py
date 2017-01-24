class BaseBuilding(object): #The word object here is optional, and doesn't change anything
    def __init__(self, name):
        self._name = name

    @property #A function that is accessed like a variable. (see line xx)
    def name(self):
        return self._name

'''
Inheritance and polymorphism is a pretty advanced concept.
To put it simply, Garage is a child of BaseBuilding.
This means that all of BaseBuilding's functions and variables are available to it.
So when a Garage is made, it inherits the 'name' variable from it's parent, BaseBuilding.

Errors:
	Errors let the rest of your program know that something bad occured.
	Example: Trying to divide by zero will throw an error
	Unless an error is expected (using a 'try' statement or 'AssertRaise'), the error will cause the program to exit
'''
class Garage(BaseBuilding): #Garage is a parent of BaseBuilding
    vehicles = [] #A list that hold multiple objects

    def enter(self, vehicle):
        if isinstance(vehicle, BaseVehicle): #Check to make sure that the vehicle that enters is a child of BaseVehicle.
            self.vehicles.append(vehicle) #Add the vehicle to the end of the vehicles list
            print('The {} has been parked in {}.'.format(vehicle.description, self.name)) #This can be read as "The " + vehicle.description + " has been parked in" + self.name
        else:
            raise TypeError('Only vehicles are allowed in garages') #This says that a TypeError occured.
    
    def __len__(self): #This overrides the python built-in len(object). len("hello") would be equal to 5
        return len(self.vehicles) #Returns the length of the vehicles array, aka how many vehicles are in the garage
   