#Implement a function that takes as input three variables, and returns the largest of the three.
print("Let's play Max Of Three! Enter three values and I'll return the largest value.")
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
    print('could not determine greatest value because 2 or more numbers are equal')
