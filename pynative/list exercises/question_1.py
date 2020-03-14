#Question 1: Given a Python list you should be able to display Python list in the following order
#Display [100, 200, 300, 400, 500] in following order: [500, 400, 300, 200, 100]
a_list = [100, 200, 300, 400, 500]
rev_list = a_list[::-1]
print(rev_list)

#or can use a for loop

a_list = [100, 200, 300, 400, 500]
rev_list = []
new_list = a_list
new_list.reverse()
for num in new_list:
	rev_list.append(num)
print(rev_list)
