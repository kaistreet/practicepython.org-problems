#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
ask_user_name = str(input("What's your name? "))
ask_user_age = int(input("And, how old are you? "))
plus_hundred = 100 - ask_user_age
print("Hi " + ask_user_name + "! It's nice to meet you. Guess what? You'll be 100 years old in " + str(plus_hundred) + " years. Isn't that cool?")
