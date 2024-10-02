print("The Love Calculator is calculating your score...")
name1 = input(" What is your name?") 
name2 = input("What is their name?") 

name_1 = name1.lower()
name_2= name2.lower()
# T R U E
T1 = name_1.count("t")
T2 = name_2.count("t")
T = T1+T2
R1 = name_1.count("r")
R2 = name_2.count("r")
R = R1+R2
U1 = name_1.count("u")
U2 = name_2.count("u")
U = U1+U2
E1 = name_1.count("e")
E2 = name_2.count("e")
E = E1+E2
total1 = T+R+U+E
#print(f"True score = {total1}")
# L O V E
L1 = name_1.count("l")
L2 = name_2.count("l")
L = L1+L2
O1 = name_1.count("o")
O2 = name_2.count("o")
O = O1+O2
V1 = name_1.count("v")
V2 = name_2.count("v")
V = V1+V2
E1 = name_1.count("e")
E2 = name_2.count("e")
E = E1+E2
total2 = L+O+V+E
#print(f"Love score = {total2}")

total3 = str(total1)+str(total2)
total4 = int(total3)
if total4 < 10 or total4 > 90:
  print(f"Your score is {total4}, you go together like coke and mentos.")
elif total4> 40 and total4 <50:
  print(f"Your score is {total4}, you are alright together.")
else:
  print(f"Your score is {total4}.") 