#Question 5: Given a string input Count all lower case, upper case, digits, and special symbols
ask_user_str = str(input('Enter a string: '))
individual_characters = []
upper_count = 0
lower_count = 0
number_count = 0
symbol_count = 0
for characters in ask_user_str:
	individual_characters.append(characters)
for things in individual_characters:
	if things.isupper() == True:
		upper_count+=1
	elif things.islower() == True:
		lower_count+=1
	elif things.isnumeric() == True:
		number_count+=1
	else:
		symbol_count+=1
print(str('count of uppercase letters: '+str(upper_count)))
print(str('count of lowercase letters: '+str(lower_count)))
print(str('count of numbers: '+str(number_count)))
print(str('count of symbols: '+str(symbol_count)))
