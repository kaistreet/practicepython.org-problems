#Problem 6.1: Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it.
class Thing:
  pass
Thing()

#second part
class Thing:
  def example():
    pass
Thing.example()

#Problem 6.2: Make a new class called Thing2 and assign the value 'abc' to a class variable called letters. Print letters.
class Thing2:
  letters = 'abc'
print(Thing2.letters)

#Problem 6.3: Make another class called Things3. Assign value 'xyz' to instance (object) attribute letters. Print letters.
class Things3:
  def __init__(self):
    self.letters = 'xyz'
something = Things3()
print(something.letters)

#Problem 6.4: Make a class called Element with instance attribute name, symbol, and number. Create an object of this class with the values 'Hydrogen', 'H', and 1.
class Element:
  def __init__(self,name,symbol,number):
    self.name = 'Hydrogen'
    self.symbol = 'H'
    self.number = 1

#Problem 6.5: Make a dictionary with these keys and values: 'name':'Hydrogren','symbol':'H','number':1. Then, create an object called hydrogren from class Element using this dictionary
element_dictionary = {'name':'Hydrogen','symbol':'H','number':1}
hydrogen = Element(element_dictionary['name'],element_dictionary['symbol'],element_dictionary['number'])
print(hydrogen.name + ' is the element name, ' + hydrogen.symbol + ' is the element symbol, and ' + str(hydrogen.number) + ' is the element number.')

#Problem 6.6: For the Element class, define a method called dump() that prints the values of the object's attributes (name, symbol and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
element_dictionary = {'name':'Hydrogen','symbol':'H','number':1}
class Element:
  def __init__(self,name,symbol,number):
    self.name = name
    self.symbol = symbol
    self.number = number
  def dump(self):
    print(self.name, self.symbol,self.number)
hydrogen = Element(**element_dictionary)
hydrogen.dump()
