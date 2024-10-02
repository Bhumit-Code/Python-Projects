# Write your code below this line 
import math
def paint_calc(height,width,cover):
    number_of_cans = (height*width)/coverage
    
    round_number = math.ceil(number_of_cans)                              #method 1
    print(f"You'll need {round_number} cans of paint.")
    """                                                                   #method 2
    if number_of_cans < round_number: 
        number_of_cans = round_number
        print(f"You'll need {number_of_cans} cans of paint.")
    elif number_of_cans > round_number:
        number_of_cans = round_number+1
        print(f"You'll need {number_of_cans} cans of paint.")
    else:
        number_of_cans = round_number
        print(f"You'll need {number_of_cans} cans of paint.")"""
    
    
# Write your code above this line 
# Define a function called paint_calc() so the code below works.   

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
