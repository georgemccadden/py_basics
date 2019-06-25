# Classes are templates, objects are instances of that class.

# I'll use coins as examples of classes and objects :

class Penny: # Defining the class.

  def __init__(self, rare=False): # Defining a class method.
    self.rare = rare

    if self.rare:
      self.value = 1.25
    else:
      self.value = 1.00


    self.value = 1.00
    self.color = "copper"
    self.num_edges = 1
    self.heads = True
  
  def rust(self):
    self.color = "greenish"

  def clean(self):
    self.color = "gold"

coin1 = Penny() # Instantiating the coin class to this coin1 object.

print(type()) # Should print <class'__main__Penny'>

coin1.value # Should print out 1.0

class Dime:
  value = 10.00
  color = "silver"
  num_edges = 1
  heads = True