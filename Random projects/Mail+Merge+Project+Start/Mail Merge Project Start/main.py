# Created a starting letter
with open("./../Mail Merge Project Start/Input/Letters/starting_letter.txt") as data:
    letter = data.read()

# Created a list of names
with open("./../Mail Merge Project Start/Input/Names/invited_names.txt") as name:
    names = name.readlines()

# Replace the [name] placeholder with the actual name.
n = 0
for name in names:
    n = n
    # Creating a new file for every name
    # Strip is used to clear the blank spaces
    with open(f"./../Mail Merge Project Start/Output/ReadyToSend/Letter_to_{names[n].strip()}.txt", mode="w") as letters:
        # Replacing each name from the list
        x = letter.replace("[name]", f"{names[n].strip()}")
        # Writing invitation Text in each letter.
        letters.write(f"{x}")
    n += 1


