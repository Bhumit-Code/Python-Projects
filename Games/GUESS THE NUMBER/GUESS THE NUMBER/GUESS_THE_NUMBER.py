import random
print("""
                                                                                                                                                           
 _____ _     _____ ____  ____    _____  _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  _ |
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\     
      """)

print("Welcome to the Number Guessing Game!")

#GUESS

def make_a_guess(Guess,Random_number):
    if Guess < Random_number:  
        print("Too low. \nGuess again.")
    elif Guess > Random_number:
        print("Too high. \nGuess again.")

ask = input("I'm thinking of the number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard':")

#EASY
def easy_game():
    Random_number = random.randint(0,101)
    attempts_left = 11
    while attempts_left <= 11:
        attempts_left -= 1
        print(f"You have {attempts_left} attempts remaining to guess the number.")    
        Guess = int(input("Make a guess: "))  
        if attempts_left == 1:
            print("You lose")
            break
        elif Guess == Random_number:
            print(f"Yay you got it. The answer was {Random_number}.")    
            break    
        make_a_guess(Guess,Random_number)
        
  
#HARD
def hard_game():
    Random_number = random.randint(0,101)
    attempts_left = 6
    while attempts_left <= 6:
        attempts_left -= 1
        print(f"You have {attempts_left} attempts remaining to guess the number.")    
        Guess = int(input("Make a guess: "))  
        if attempts_left == 1:
            print("You lose")
            break
        elif Guess == Random_number:
            print(f"Yay you got it. The answer was {Random_number}.")    
            break    
        make_a_guess(Guess,Random_number)    

#EASY OR HARD        
if ask == "easy":
    easy_game()
elif ask == "hard":
    hard_game()    
else:
    print("Wrong input!")
       







    
