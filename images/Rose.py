# Number game challenge!
#Players get 5 guesses.
#They must guess a random number.
#It has to be a whole number from 1 to 100
#Tell them if they are too high or too low if they guess wrong
#Tell them how many guesses they have made

import random


random_number = random.randint(1,10)
tries = 0
tries_remaining = 5


while tries < 5:
  guess = input("Guess a number between 1 and 10")
  tries += 1
  tries_remaining -= 1

  try:
    guess_num = int(guess)
  except:
    print("That's not a whole number!")
    break

  if not guess_num > 0 or not guess_num < 11:
    print("That number is not between 1 and 10.")
    break



  elif guess_num == random_number:
    print("Congratulations! No one cares if you got it correct!")
    print("It took you {} tries.".format(tries))
    break


  elif guess_num < random_number:
    if tries_remaining > 0:
      print("I'm sorry loser, that number is low. You have {} tries remaining.".format(int(tries_remaining)))
      continue
    else:
      print("Sorry, but my number was {}".format(random_number))
      print("You are out of tries. Better luck next time dumby.")



  elif guess_num > random_number:
    if tries_remaining > 0:
      print("I'm sorry loser, that number is high. You have {} tries remaining.".format(int(tries_remaining)))
      continue
    else:
      print("Sorry, but my number was {}".format(random_number))
      print("You are out of tries. Better luck next time loser.")







