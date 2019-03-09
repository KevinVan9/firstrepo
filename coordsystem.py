'''A coordinate system for fun and to learn classes and obhects in python'''
class coord:
	def __init__(self, x , y): #Creates an instance of the class initialised with x and y
		self.x = x
		self.y = y

	def __str__(self): #Gives a nice description of the object when printed out
		return ("({}, {})".format(self.x, self.y))

	def __add__(self, other): #A method that adds two coordinates together
		a = self.x + other.x
		b = self.y + other.y
		return coord(a, b)


a = coord(1, 4)
b = coord(3, 2)
print(a+b)