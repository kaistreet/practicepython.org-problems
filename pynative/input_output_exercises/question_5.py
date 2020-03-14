#Question 5: Accept list of 5 float numbers as a input from user
def five_number_list():
	number_list = []
	ask_user_number = float(input('Enter a floating point number: '))
	number_list.append(ask_user_number)
	while len(number_list) < 5:
		ask_user_number = float(input('Enter another floating point number: '))
		number_list.append(ask_user_number)
	else:
		print('Program done.')
		print(str("Here's your list of numbers: ")+str(number_list))
five_number_list()
