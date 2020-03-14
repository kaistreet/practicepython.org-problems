#Question 3: Accept n number from user and calculate the sum of all number between 1 and n including n
ask_user_number = int(input('Enter a number from 1 to 10: '))
range_num_list = []
for num in range(ask_user_number+1):
	range_num_list.append(num)
print(sum(range_num_list))
