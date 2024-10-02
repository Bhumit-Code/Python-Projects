
water = 500
milk = 500
coffee = 500 
money = 0

while True:
    Type = input("What would you like? (espresso/latte/cappuccino):").lower()
    water = water
    milk = milk
    coffee = coffee 
    money = money
    if Type == "espresso":
        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money_e = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01) 
        if money_e >= 1.50:
            if water >= 50:
                if coffee >= 18:
   
                    water -= 50
                    coffee -= 18
                    change = round((money_e - 1.50),2)
                    money += 1.50
                    print(f"Here is {change}$ in change.")
                    print("Here's your espresso!")
                else:
                    print("No enough coffee! Money Refunded")
            else:
                print("No enough water! Money Refunded")
        else:
            print("No enough money! Money Refunded")            
        #print(f"{water},{milk},{coffee},{money}")
        
            
             
        
    elif Type == "latte":
        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money_l = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        if money_l >= 1.50:
            if water >= 200:
                if coffee >= 24:
                    if milk >= 150:
                    
                        water -= 200
                        coffee -= 24
                        milk -= 150
                        change = round((money_l - 2.50),2)
                        money += 2.50
                        print(f"Here is {change}$ in change.")
                        print("Here's your latte!")
                    else:
                        print("No enough milk! Money Refunded")
                else:
                    print("No enough coffee! Money Refunded")
            else:
                print("No enough water! Money Refunded")
        else:
            print("No enough money! Money Refunded")        
        #print(f"{water},{milk},{coffee},{money}")
        
      

    elif Type == "cappuccino":
        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money_c = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        if money_c >= 1.50:
            if water >= 250:
                if coffee >= 24:
                    if milk >= 100:
                    
                        water -= 250
                        coffee -= 24
                        milk -= 100
                        change = round((money_c - 3.00),2)
                        money += 3.00
                        print(f"Here is {change}$ in change.")
                        print("Here's your cappuccino!")
                    else:
                        print("No enough milk! Money Refunded")
                else:
                    print("No enough coffee! Money Refunded")
            else:
                print("No enough water! Money Refunded")
        else:
            print("No enough money! Money Refunded")        
        #print(f"{water},{milk},{coffee},{money}")

    if Type == "report":
        print(f"water:{water}\n"
             f"milk:{milk}\n"
             f"coffee:{coffee}\n"
             f"money:{money}")
        
    if Type == "turnoff":
        print("Turning off .....")
        break