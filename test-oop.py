#illustrate how to create a class and use it

class example:
	x=0
	def party(self): #by convention, at least input argument self is required
		self.x=self.x+1
		print "So far", self.x 

a=example() #instantiate an object
print "type", type(a)
print "dir", dir(a)


