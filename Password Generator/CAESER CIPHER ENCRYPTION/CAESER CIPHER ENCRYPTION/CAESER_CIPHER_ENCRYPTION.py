alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text_1,shift_1):
    list1 = []
    list2 = []
    
    for letter in text_1:
        index = alphabet.index(letter)
        list1.append(index)
        
        shifting =index + shift_1
        list2.append(shifting)

    output = [alphabet[i] for i in list2]
    output = ''.join(output)
    print("Here's the encoded result:",output)
        


def decode(text_2,shift_2):
    list3 = []
    list4 = []
    
    for letter2 in text_2:
        index2 = alphabet.index(letter2)
        list3.append(index2)
        
        shifting2 =index2 - shift_2
        list4.append(shifting2)

    output = [alphabet[i] for i in list4]
    output = ''.join(output)
    print("Here's the decoded result:",output)
        

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text_1=text,shift_1=shift)
    elif direction == "decode":
        decode(text_2=text,shift_2=shift)
    else:
        print("Direction input is wrong!")

    
    ask = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if ask == "yes":
        print("Again") 
    elif ask == "no":
        print("Good bye")
        break
    else:
        print("Wrong input!")
        break