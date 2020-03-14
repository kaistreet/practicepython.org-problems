#Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
ask_user_str = str(input('Enter a string: '))
ask_user_str_2 = str(input('Enter another string: '))
half_string = int(len(ask_user_str)/2)
new_string = str(ask_user_str[0:half_string])+str(ask_user_str_2)+str(ask_user_str[half_string:])
print(new_string)
