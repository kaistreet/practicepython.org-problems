#Question 4: Concatenate two lists in the following order
list1 = ["Hello ", "There"]
list2 = ["Dear ", "Sir"]
list3 = []
for word,thing in list1,list2:
	list3.append(word+thing)
print(list3)
