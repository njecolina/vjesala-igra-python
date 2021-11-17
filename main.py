import random
from vjesala_art import logo, stages
print(logo)
from vjesala_rijeci import word_list

chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"

lives = 6
end = False

while not end:
  print(stages[lives])
  print(f"Preostalo života: {lives}\n")
  print(f"{' '.join(display)}")
  guess = input("\nPogodi slovo: ").lower()

  if guess in display:
    print(f"\nVeć ste probali slovo {guess}, probajte opet neko drugo slovo! ;)\n")

  for position in range(word_length):
    slovo = chosen_word[position]
    if slovo == guess:
      display[position] = slovo
    
  if guess not in chosen_word:
    print(f"\nSlovo {guess} nije u traženoj riječi! Jedan život manje. :/")
    lives -= 1
    if lives == 0:
      end = True
      print("\nUmro čovjek. :( Gotova igra.\nTražena riječ je bila - " + chosen_word + ".")
  
  if "_" not in display:
    end = True
    print("\nPOBJEDA!! ČOVJEK JE SPAŠEN! HVALA TI NA IGRANJU! TI SI SUPER! xoxo")
