#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
ask_user_number = int(input('Choose a number to find its divisors: '))
listrange = list(range(1,ask_user_number+1))
divisors = []
for number in listrange:
  if ask_user_number % number == 0:
    divisors.append(number)
print(divisors)
