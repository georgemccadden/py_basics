# Classes are templates, objects are instances of that class.

# I'll use coins as examples of classes and objects :

class Penny: # Defining the class.
  value = 1.00
  color = "copper"
  num_edges = 1
  heads = True

coin1 = Penny() # Instantiating the coin class to this coin1 object.

print(type()) # Should print <class'__main__Penny'>

coin1.value # Should print out 1.0

class Dime:
  value = 10.00
  color = "silver"
  num_edges = 1
  heads = True