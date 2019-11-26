#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
a = [5, 10, 15, 20, 25]
b = []
def first_last():
    num_1 = a[0]
    num_2 = a[-1]
    b.append(num_1)
    b.append(num_2)
    print(b)
first_last()
