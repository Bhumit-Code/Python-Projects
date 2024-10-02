import random 
print("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.")
Choose = int(input(""))
Computer = random.randint(0,2)


#Input from user
# Rock
if Choose == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

# Paper
elif Choose == 1:    
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

# Scissors
elif Choose == 2:    
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    

#Inpit from Computer
if Computer == 0:
    print("Computer chose:\n\n"
          """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

elif Computer == 1:    
    print("Computer chose:\n\n"
          """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


elif Computer == 2:    
    print("Computer chose:\n\n"
          """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    
    
if Computer ==0 and Choose == 0:
    print("Its draw")
elif Computer ==1 and Choose == 1:
    print("Its draw")
elif Computer ==2 and Choose == 2:
    print("Its draw")
elif Computer == 0 and Choose == 2:
    print("You lose!")
elif Computer == 2 and Choose == 1:
    print("You lose!")
elif Computer == 1 and Choose == 0:
    print("You lose!")
elif Computer == 2 and Choose == 0:
    print("You Win!")
elif Computer == 1 and Choose == 2:
    print("You Win!")
elif Computer == 0 and Choose == 1:
    print("You Win!")