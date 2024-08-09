import random

# create a list which is contaning 5-letter words

word_list= ["power", "house", "chair", "phone", "light", "music", "enjoy", "trust"]

# choose a random word from the list

len_of_list = len(word_list)

chosen_word = word_list[random.randint(0, len_of_list - 1)]

# create "placeholder" and print "_" for each letter in the chosen word

placeholder=""
for s in range(0, len(chosen_word)):
    placeholder = placeholder + " _ "

print(placeholder + "\n")

# The game is starting....

print("You have 6 lives to guess the word. \n")

game_over = False
correct_letters = []
lives = 6
# 
while not game_over:

  guess = input("Guess a letter: ").lower()
  display = ""
  
  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
      
    elif letter in correct_letters:
      display += letter

    else:
      display += " _ "
      print("\n")
  
  print(display)

  if " _ " not in display:
    game_over = True
    print("You win!")

  if guess not in chosen_word:
    print("\nYou lose a life.\n")
    lives -= 1

    if lives == 0:
      game_over = True
      print("You lose :(")