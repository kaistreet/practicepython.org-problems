#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def next_number():
    ask_user_number = int(input('Enter the number you want the next icrement of: '))
    increment = ask_user_number+1
    print(str(increment)+' is the next increment after '+str(ask_user_number)+'.')
next_number()
