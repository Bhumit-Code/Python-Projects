import random
print(""" _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/""")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
ASK = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
#Start
score_U = 0 
while score_U < 21:
    if ASK == "y":
        #for user
        rand_cards = random.sample(cards,len(cards))
        rand_card_U = random.sample(rand_cards,2)
        current_score_U= rand_card_U[0]+rand_card_U[1]
        score_U = current_score_U
        
        #for computer
        rand_card_C = random.sample(rand_cards,1)
        current_score_C= rand_card_C[0]
        print(f"Your cards: {rand_card_U}, current score: {current_score_U}")
        print(f"Computer's first card: {current_score_C}")
    
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card == "y":
        #for user
            rand_card_U = rand_card_U + random.sample(rand_cards,1)
            current_score_U = rand_card_U[0] + rand_card_U[1] + rand_card_U[2]
            score_U = current_score_U
            print(f"Your cards: {rand_card_U}, current score: {current_score_U}")
            print(f"Computer's first card: {current_score_C}")
            
            if score_U <= 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass:")
                if another_card == "y":
                #for user
                    rand_card_U = rand_card_U + random.sample(rand_cards,1)
                    current_score_U = rand_card_U[0] + rand_card_U[1] + rand_card_U[2] + rand_card_U[3]
                    score_U = current_score_U
                    print(f"Your cards: {rand_card_U}, current score: {current_score_U}")
                    if current_score_C > current_score_U and current_score_C <= 21:
                            print("Computer Win!")
                    else:
                            print("You Won!")
                    break
                elif another_card == "n":
                    rand_card_C = rand_card_C+ random.sample(rand_cards,1)
                    current_score_C = rand_card_C[0]+rand_card_C[1]
                    if  current_score_C <= 21:
                        rand_card_C = rand_card_C + random.sample(rand_cards,1)
                        current_score_C = rand_card_C[0]+rand_card_C[1]+rand_card_C[2]
                        print(f"Computer's final hand: {rand_card_C}, Final score:{current_score_C}")    
                        
                        if current_score_C > current_score_U and current_score_C <= 21:
                            print("Computer Win!")
                        else:
                            print("You Won!")
                        break
                    else:
                        break

            elif score_U > 21:
                print("You went over. You Lose!")
        
        elif another_card == "n":
            rand_card_C = rand_card_C+ random.sample(rand_cards,1)
            current_score_C = rand_card_C[0]+rand_card_C[1]
            print(f"Your final hand: {rand_card_U}, final score: {current_score_U}")

            if  current_score_C <= 21:
                rand_card_C = rand_card_C + random.sample(rand_cards,1)
                current_score_C = rand_card_C[0]+rand_card_C[1]+rand_card_C[2]
                print(f"Computer's final hand: {rand_card_C}, Final score:{current_score_C}")    
                
                if current_score_C > current_score_U and current_score_C <= 21:
                    print("Computer Win!")
                else:
                    print("You Won!")
                break
            else:
                break
    
    elif ASK == "n":
        print("OK BYE!")
        break
 


