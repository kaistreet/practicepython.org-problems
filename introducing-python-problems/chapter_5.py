#Problem 5.1: Make a file called zoo.py. In it define a function called hours that prints the string 'Open 9-5 daily'. Then, use the interpreter to import the zoo module and call its hours function.
#where zoo.py is:
def hours():
  print('Open 9-5 daily')

import zoo
zoo.hours()

#Problem 5.2: In the interpreter, import the zoo module as menagerie and call its hours function
#where zoo.py is:
def hours():
  print('Open 9-5 daily')
	
import zoo as menagerie
menagerie.hours()

#Problem 5.3: Import the hours function directly from zoo and call it.
from zoo import hours
hours()

#Problem 5.4: Import the hours() function as info and call it
from zoo import hours as info
info()

#Problem 5.5: Make a dictionary called plain with the key-vlaue pairs 'a':1,'b':2,'c':3 and print it.
plain = {'a':1,'b':2,'c':3}
print(plain)

#Problem 5.6: Make an OrderedDict called fancy from the same pairs and print it.
from collections import OrderedDict
fancy = OrderedDict([('a',1),('b',2),('c',3)])
print(fancy)

#Problem 5.7: Make a defaultDict called dict_of_lists and pass it the argument list. Make the list dict_of_list['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a']
from collections import defaultdict
dictoflists = defaultdict(list)
dictoflists['a'].append('something for a')
print(dictoflists['a'])
