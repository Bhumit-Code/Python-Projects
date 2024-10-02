from os import name
from ascii import art,Vs
from get_data import data
import random

#access items in list
n = 0
list1 = []

for items in data:
    items = (data[n]["name"],
                    data[n]["follower_count"],
                     data[n]["description"],
                         data[n]["country"])
    n +=1
    list1.append(items)
#print(list1)
score = 1
CompareB = random.sample(list1,1)
while True:
    CompareA = CompareB
    CompareB = random.sample(list1,1)

    while CompareA == CompareB:
        CompareA = random.sample(list1,1)
        CompareB = random.sample(list1,1)
    print(art)
    print("Comapre A :",CompareA[0][0],",",CompareA[0][2],",",CompareA[0][3])
    print(Vs)
    print("Comapre B :",CompareB[0][0],",",CompareB[0][2],",",CompareB[0][3])

    score = score
    ask = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n"*20)
    if CompareA[0][1] > CompareB[0][1] and ask == 'A':
        print(f"Your're right! Current score: {score}")
        score = score+1
    elif CompareA[0][1] < CompareB[0][1] and ask == 'B':
        print(f"Your're right! Current score: {score}")
        score = score+1
    else:    
        print(f"Sorry, that's wrong. Final score is: {score-1}")
        break
