#Question 3: Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string
s1 = str(input('Enter a string: '))
s2 = str(input('Enter another string: '))
new_string = str(s1[0]+s1[int(len(s1)/2)]+s1[-1]+s2[0]+s2[int(len(s2)/2)]+s2[-1])
print(new_string)
