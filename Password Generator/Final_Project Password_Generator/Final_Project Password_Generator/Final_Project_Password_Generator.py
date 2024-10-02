import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

p_letters = int(input("How many letters would you like in your password?"))
l_sample= random.sample(letters,p_letters)

p_symbols = int(input("How many symbols would you like?"))
s_sample = random.sample(symbols,p_symbols)

p_numbers = int(input("How many number would you like?"))
n_number = random.sample(numbers,p_numbers)


overall_sample= l_sample+s_sample+n_number
password = random.sample(overall_sample,len(overall_sample))

joint = ''.join(password)
print("Here is your password:",joint)