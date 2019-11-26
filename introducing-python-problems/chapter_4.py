#Problem 4.1: Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, 'just right' if equal to 7
guess_me = 7
user_guess = int(input('Guess the number: '))
if user_guess > guess_me:
  print('too high')
elif user_guess < guess_me:
  print('too low')
else:
  print('just right')

#Problem 4.2: Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print 'too low' if start is less then guess_me. If start equals guess_me, print 'found it' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
guess_me = 7
start = 1
while True:
  if start < guess_me:
    print('too low')
  elif start == guess_me:
    print('found it')
    break
  elif start > guess_me:
    print('oops')
    break
  start += 1

#Problem 4.3: Use a for loop to print the values of the list [3, 2, 1, 0].
numbers = [3,2,1,0]
for num in numbers:
  print(numbers)

#Problem 4.4: Use a list comprehension to make a list of the even numbers in range(10)
numbers = [num for num in range(10) if num % 2 == 0]
print(numbers)

#Problem 4.5: Use a dictionary comprehension to create the dictionary squares. Use range (10) to return the keys and use the square of each key as its value.
squares = {sq: sq*sq for sq in range(10)}
print(squares)

#Problem 4.6: Use a set comprehension to create the set odd from the odd numbers in range(10).
odd = {num for num in range(10) if num % 2 == 1}
print(odd)

#Problem 4.7: Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.
for gotstring in ('Got %s' % num for num in range(10)):
  print(gotstring)

#Problem 4.8: Define a function called good that returns the list ['Harry','Ron','Hermione']
def good():
  characters = ['Harry','Ron','Hermione']
  print(characters)
good()

#Problem 4.9: Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
def get_odds():
  numbers = [num for num in range(10) if num % 2 == 1]
  print(numbers[2])
get_odds()

#Problem 4.10: Define a decorator called test that prints 'start' when a function is called and 'end' when it finishes.
def test(func):
    def new_func(*var, **vars):
        print('start')
        result = func(*var, **vars)
        print('end')
        return result
    return new_func

@test
def something():
    print('this is a new function')
something()

#Problem 4.11: Define an exception called OopsException. Raise this excpetion to see what happens. Then write the code to catch this exception and print 'Caught an oops'.

#Problem 4.12: Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit','Crewel Fate'] and plots = ['A nun turns into a monster','A haunted yarn shop'].
titles = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a monster','A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)
