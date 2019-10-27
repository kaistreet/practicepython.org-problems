#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
def element_search():
    num_list = [num for num in range(21)]
    extra_num = int(input("Enter a number to see if it's in this range: "))
    if extra_num in num_list:
        print(True)
    else:
        print(False)
element_search()
