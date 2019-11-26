#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
def palindrome_checker(): 
    ask_user_word = str(input("Choose your word to check if it's a palindrome or not: "))
    if ask_user_word == ask_user_word[::-1]:
        print('this is a palindrome')
    else:
        print("this isn't a palindrome")
palindrome_checker()
play_again = str(input('would you like to check again? [enter y or n]'))
y = 'y'
while play_again == y:
    palindrome_checker()
    play_again = str(input('would you like to check again? [enter y or n]: '))
    y = 'y'
else:
    print('have a good day!')
