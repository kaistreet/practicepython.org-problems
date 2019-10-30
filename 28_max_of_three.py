#Implement a function that takes as input three variables, and returns the largest of the three.
print("Let's play Max Of Three! Enter three values and I'll return the largest value.")
def max_of_three():
    value1 = int(input('Enter a value: '))
    value2 = int(input('Enter a value: '))
    value3 = int(input('Enter a value: '))
    if value1 > value2 and value1 > value3:
       print(str(value1)+' was the greatest value')
    elif value2 > value1 and value2 > value3:
        print(str(value2)+' was the greatest value')
    elif value3 > value1 and value3 > value2:
        print(str(value3)+' was the greatest value')
    else:
        print('Could not determine the greatest value because 2 or more numbers are equal.')
max_of_three()
play_again = str(input('Would you like to play Max of Three again? [Press y to play again] '))
while play_again == 'y':
    max_of_three()
    play_again = str(input('Would you like to play Max of Three again? [Press y to play again] '))
else:
    print('I hope you enjoyed playing Max Of Three.')
