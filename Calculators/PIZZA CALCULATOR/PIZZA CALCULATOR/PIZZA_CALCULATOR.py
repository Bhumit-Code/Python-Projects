print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L  ") 
add_pepperoni = input("Do you want pepperoni? Y or N  ") 
extra_cheese = input("Do you want extra cheese? Y or N  ")  

S = 15
M = 20
L = 25
Add_pepperoni_S = 2
Add_pepperoni_M_L = 3
Add_extra_cheese = 1

if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        Bill  = S + Add_pepperoni_S + Add_extra_cheese
    elif add_pepperoni == "Y" and extra_cheese == "N":
        Bill = S + Add_pepperoni_S   
    elif add_pepperoni == "N" and extra_cheese == "Y":
        Bill = S + Add_extra_cheese
    else:
        Bill = S    
  


#MEDIUM PIZZA
if size == "M":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        Bill  = M + Add_pepperoni_M_L + Add_extra_cheese
    elif add_pepperoni == "Y" and extra_cheese == "N":
        Bill = M + Add_pepperoni_M_L   
    elif add_pepperoni == "N" and extra_cheese == "Y":
        Bill = M + Add_extra_cheese
    else:
        Bill = M    
  


#LARGE PIZZA
if size == "L":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        Bill  = L + Add_pepperoni_M_L + Add_extra_cheese
    elif add_pepperoni == "Y" and extra_cheese == "N":
        Bill = L + Add_pepperoni_M_L   
    elif add_pepperoni == "N" and extra_cheese == "Y":
        Bill = L + Add_extra_cheese
    else:
        Bill = L    
  
print(f"Your final bill is: ${Bill}.")


