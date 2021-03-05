import numbers
import words

print("*********************************")
print('========Chosse the game!=======')
print("*********************************")

print('(1) SPELLING WORDS   (2) NUMBERS')
game = int(input('Which game? '))

if game ==1:
  print('Spelling Words game!')
  words.play()
elif game ==2:
  print('Numbers game!')
  numbers.play()
