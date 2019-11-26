#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
ask_user_number = int(input('Guess a number: '))
if ask_user_number % 2 == 0:
  print('Your number is even!')
elif ask_user_number % 2 == 1:
  print('Your number is odd!')
elif ask_user_number == 0:
  print('Your number is zero!')
else:
  print("this isn't a number")
