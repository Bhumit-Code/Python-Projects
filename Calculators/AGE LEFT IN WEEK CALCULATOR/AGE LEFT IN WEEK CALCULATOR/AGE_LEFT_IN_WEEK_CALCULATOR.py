#Input age
age = input("Write your age here: ")
#Convert age str to int and into weeks 
weeks_of_age = int(age)*52
#Count age left in week from age 90
weeks_left = (90*52)-(weeks_of_age)
print(f"You have {weeks_left} weeks left." )
