import random

def play():

  print("*********************************")
  print("WELCOME TO CHOOSE NUMBER GAME!")
  print("*********************************")

  secret_number = random.randrange(1,101)
  total_tempt = 0
  points = 1000

  print("Choose the difficulty!")
  print("(1) Easy (2) Hard (3) Extreme")

  level = int(input("Which difficulty?: "))

  if(level == 1):
      total_tempt = 20
  elif(level == 2):
      total_tempt = 10
  else:
      total_tempt = 5

  for round in range(1, total_tempt + 1):
      print(f'Attempt {round} of {total_tempt}')

      shot_str = input("Type a number between 1 and 100: ")
      print("You typed ", shot_str)
      shot_attempt = int(shot_str)

      if(shot_attempt < 1 or shot_attempt > 100):
          print("Type a number between 1 and 100!")
          continue

      win = shot_attempt == secret_number
      bigger   = shot_attempt > secret_number
      smaller   = shot_attempt < secret_number

      if(win):
          print(f'You win and received {points_received} points!')
          break
      else:
          if(bigger):
              print("You missed! Your shot is bigger that the secret number.")
          elif(smaller):
              print("You missed! Your shot is smaller that the secret number.")
          points_lost = abs(secret_number - shot_attempt)
          points_received = points - points_lost

  print("END GAME")
  print (f'The secret number is: {secret_number}')
if(__name__=='__main__'):
  play()
