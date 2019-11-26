#Ask the user for a number and determine whether the number is prime or not.
ask_number = int(input('Enter a number to determine its primality: '))
prime_checker = [num for num in range(2, ask_number) if ask_number % num == 0]
if ask_number <= 0:
  print('this is not prime')
elif ask_number > 1:
  if len(prime_checker) == 0:
    print('this is prime')
  else:
      print('this is not prime')
else:
  print('this is not prime')
