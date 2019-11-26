#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
import sys
def number_guess():
  num = random.randint(1,9)
  ask_number = int(input('Guess the number: '))
  if ask_number == num:
    print('exactly right')
  elif ask_number < num:
    print('too low')
  elif ask_number > num:
    print('too high')
  else:
    sys.exit()
number_guess()
play_again = str(input('want to play again? '))
y = ['y','ya','yea','yeah','yes','yup']
while play_again in y:
  number_guess()
  play_again = str(input('want to play again? '))
else:
  print('ok, hope you had fun!')
  sys.exit()
