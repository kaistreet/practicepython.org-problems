#Create a function that takes a list and returns the first element.
def first_element_return():
    element_list = []
    user_element_1 = str(input('Enter an element to add to the list: '))
    user_element_2 = str(input('Enter another element to add to the list: '))
    user_element_3 = str(input('Enter another element to add to the list: '))
    element_list.append(user_element_1)
    element_list.append(user_element_2)
    element_list.append(user_element_3)
    print('first element in the list is: 'element_list[0])
first_element_return()
