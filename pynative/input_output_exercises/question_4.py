#Question 4: Display float number with 2 decimal places using print()
ask_user_num = float(input('Enter a number with more than 2 decimal places: '))
print(str('Your number in decimal format (with two decimal places) is ')+str(float('%.2f' % ask_user_num)))
