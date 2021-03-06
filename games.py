import numbers
import words

print("*********************************")
print('========Chosse the game!=======')
print("*********************************")

print('(1) SPELLING WORDS   (2) NUMBERS')
game = int(input('Which game? '))

if game ==1:
  print('Guess the Word game!')
  words.play()
elif game ==2:
  print('Numbers game!')
  numbers.play()
