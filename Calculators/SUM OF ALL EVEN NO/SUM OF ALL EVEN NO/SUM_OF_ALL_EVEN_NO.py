target = int(input())

sum = 0
for x in range(1,target+1):
    if x % 2 == 0:
        sum = x+sum
    
print(sum)
    
