#Problem 3.1: Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday.
years_list = [1990,1991,1992,1993,1994,1995]
print(years_list)

#Problem 3.2: In which year in years_list was your third birthday?
years_list = [1990,1991,1992,1993,1994,1995]
print(years_list[3])

#Problem 3.3: In which year in years_list were you the oldest?
years_list = [1990,1991,1992,1993,1994,1995]
print(max(years_list))

"""Alternatively you can use the following script"""
years_list = [1990,1991,1992,1993,1994,1995]
print(years_list[-1])

#Problem 3.4: Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella"
things =["mozzarella","cinderella","salmonella"]
print(things)

#Problem 3.5: Capitalize the elements in things that refers to a person, then print the list.
things =["mozzarella","cinderella","salmonella"]
things[1] = things[1].capitalize()
print(things)

#Problem 3.6: Make the cheesy element of things uppercase, then print the list.
things =["mozzarella","cinderella","salmonella"]
things[0] = things[0].upper()
print(things)

#Problem 3.7: Delete the disease element from things, collect your Nobel Prize, then print the list.
things =["mozzarella","cinderella","salmonella"]
del things[2]
print("You won a Nobel Prize! Here's what's left in your list: ")
print(things)

#Problem 3.8: Create a list called surprise with the elements "Groucho", "Chico" and "Harpo"
surprise = ["Groucho","Chico","Harpo"]
print(surprise)

#Problem 3.9: Lowercase the last element of the surprise list, reverse it, then capitalize it.
surprise = ["Groucho","Chico","Harpo"]
harpo_surprise = surprise[2].lower()
harpo_surprise = harpo_surprise[::-1]
surprise[2] = harpo_surprise.lower().capitalize()
print(surprise)

#Problem 3.10: Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f)

#Problem 3.11: Using your three-word dictionary e2f, print the French word for walrus.
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f.get("walrus"))

"""Alternatively you can use the following script"""
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f["walrus"])

#Problem 3.12: Make a French-to-English dictionary called f2e from e2f. Use the items method.
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
f2e = {french:english for english, french in e2f.items()}
print(f2e)

#Problem 3.13: Using f2e, print the English equivalent of the French word chien.
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
f2e ={french:english for english,french in e2f.items()}
print(f2e["chien"])

#Problem 3.14: Make and print a set of English words from the keys in e2f.
e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
f2e ={french:english for english,french in e2f.items()}
print(f2e.keys())

#Problem 3.15: Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':[],'emus':[]},'plants':{},'other':{}}
print(life)

#Problem 3.16: Print the top-level keys of life.
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':[],'emus':[]},'plants':{},'other':{}}
print(life.keys())

#Problem 3.17: Print the keys for life['animals'].
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':[],'emus':[]},'plants':{},'other':{}}
print(life['animals'].keys())

#Problem 3.18: Print the values for life['animals']['cats'].
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':[],'emus':[]},'plants':{},'other':{}}
print(life['animals']['cats'])
