print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island.\n"
"Your mission is to find the treasure.\n"
"You're at a cross road.")
L1_R1= input("Where do you want to go? Type 'left' or 'right': \n").lower()
if L1_R1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    L2_R2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if L2_R2 == "wait":
        print("You arrive at the island unharmed. Ther is a house with 3 doors.\n"
              "One red, one yellow and one blue.")
        RGB_Door = input("Which color do you choose?").lower()
        if RGB_Door == "yellow":
            print("You Win!")
        elif RGB_Door == "red" or RGB_Door == "blue":
            print("You enter a room of beasts. Game Over")
    elif L2_R2 == "swim":
        print("Game over")
    else:
        print("Wrong input!")    


elif L1_R1 == "right":
    print("game over")
else:
    print("Wrong input!")


    

