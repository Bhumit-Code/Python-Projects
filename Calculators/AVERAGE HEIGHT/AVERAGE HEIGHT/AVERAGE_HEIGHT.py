
student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height=0
for y in student_heights:
    total_height += y
   

no_of_stud = 0
for students in student_heights:
    no_of_stud += 1


avg_height = round(total_height/no_of_stud)

print("total height =", str(total_height))
print("number of students =", str(no_of_stud))
print("average height =", str(avg_height))
    
  
    