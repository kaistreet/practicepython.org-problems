#Question 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3 = list2[::-1]
for thing,thing2 in zip(list1,list3):
	print(thing,thing2)
