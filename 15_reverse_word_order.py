#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
def word_reverser():
  ask_user_string = str(input("Write a sentence and I'll write it in reverse: "))
  new_string = ask_user_string.split()
  new_string = new_string[::-1]
  reversed_string = " ".join(new_string)
  print(reversed_string)
word_reverser()
