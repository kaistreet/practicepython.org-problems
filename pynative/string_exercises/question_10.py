#Question 10: Given an input string, count occurrences of all characters within a string
ask_user_str = str(input('Enter a string: '))
str_characters = []
for characters in ask_user_str:
	str_characters.append(characters)
for things in str_characters:
	print(str(things)+': '+str(str_characters.count(things)))
