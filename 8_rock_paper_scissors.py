#Make a two-player Rock-Paper-Scissors game.
import sys
player_1 = str(input('Player 1, enter your name: '))
print('Hi ' + player_1 + '!')
player_2 = str(input('Player 2, enter your name: '))
print('Hi ' + player_2 + '!')
y = ['y','yes','yup','yeah','yea']
ready_p1 = str(input(player_1 + ', are you ready?'))
if ready_p1 in y:
  print('ok!')
  ready_p2 = str(input(player_2 + ', are you ready?'))
  if ready_p2 in y:
    print('ok!')
else:
  print("alright, we won't play then.")
  sys.exit()
rock = ['rock','r']
paper = ['paper','p']
scissors = ['scissors','s']
rps_1 = str(input(player_1 + '! Rock, Paper or Scissors?'))
rps_2 = str(input(player_2 + '! Rock, Paper or Scissors?'))
if rps_1 in rock and rps_2 in scissors:
  print('')
elif rps_1 in paper and rps_2 in rock:
  print('')
elif rps_1 in scissors and rps_2 in paper:
  print('')
elif rps_1 == rps_2:
  print("it's a tie!")
