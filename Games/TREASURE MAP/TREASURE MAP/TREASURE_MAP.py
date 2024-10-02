line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("") 

letter = position[0].lower()
print(letter)
abc = ['a','b','c']
letter_index = abc.index(letter)
print(letter_index)
number_index = int(position[1])-1
print(number_index)
map[letter_index][number_index] = 'X'
#if position == "A1":
#    line1[0]="X"
#elif position == "A2":
#    line2[0]="X"
#elif position == "A3":
#    line3[0]="X"
#elif position == "B1":
#    line1[1]="X"
#elif position == "B2":
#    line2[1]="X"
#elif position == "B3":
#    line3[1]="X"
#elif position == "C1":
#    line1[2]="X"
#elif position == "C2":
#    line2[2]="X"
#elif position == "C3":
#    line3[2]="X"

print(f"{line1}\n{line2}\n{line3}")
