#Greetings and ask for total amt of Bill
print("Welcome to the tip calculator!")
#Input Bill amount
Bill = int(input("What was the total bill? "))
#How much percent of tip
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
#How many people slipt the bill
people = int(input("How many people to split the bill? "))
#Count percentage and subtract it from bill
percent = Bill*(tip/100)
#Divide the bill by no. of people
total_per_person = (Bill - percent)/people
print(f"Each person should pay: ${total_per_person}")