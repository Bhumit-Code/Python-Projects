#Input weight
weight = input("Write your weight here:")
#Input height
height = input("Write your height here:")
#Convert Weight and height from string to int and float
weight_int = int(weight)
height_float = float(height)
#write the formula for BMI calculator as per PEMDAS
BMI = round(weight_int/(height_float**2))
print(f"Your BMI is : {BMI}")
