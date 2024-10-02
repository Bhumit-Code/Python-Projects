import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]
lives = 6

Choosen_word = random.choice(word_list)
print(Choosen_word)
length = len(Choosen_word)

display = []
for space in Choosen_word:
    display.append("_")    
print(display)
   
end = False
while not end:
    guess = input("Guess a letter!").lower()

    for position in range(length):
        letter = Choosen_word[position]
        if letter == guess:
            display[position] = letter
                
    print(display)   
    
    if guess not in Choosen_word:
        lives -=1
        if lives==0:
            print("You lose!")
            break
    if "_" not in display:
        print("You won!")
        break
    print(stages[lives])