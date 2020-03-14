#Question 7: String characters balance Test; String s1 and s2 is balanced if all the chars in the string1 are there in s2. characters position doesn’t matter.
s1 = str(input('Enter a string: '))
s2 = str(input('Enter another string: '))
s1_list = []
s2_list = []
balance_status = []
for s1_characters in s1:
	s1_list.append(s1_characters)
for s2_characters in s2:
	s2_list.append(s2_characters)
for characters in s1_list:
	if characters in s2_list:
		balance_status.append('strings are balanced')
	else:
		balance_status.append('strings are not balanced')
balance_status = list(set(balance_status))
print(str(balance_status).replace("[","").replace("'","").replace("]",""))
