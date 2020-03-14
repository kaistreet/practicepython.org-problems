#Question 4: arrange String characters such that lowercase letters should come first
ask_user_str = str(input('Enter a string: ')).title()
lower = []
upper = []
for characters in ask_user_str:
	if characters.islower() == True:
		lower.append(characters)
	else:
		upper.append(characters)
low = str(lower)
up = str(upper)
new_string = str(low+up).replace("[","").replace("'","").replace(",","").replace("]","").replace(" ","")
print(new_string)
