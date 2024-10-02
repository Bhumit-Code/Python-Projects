import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
final_dict = {row.letter: row.code for index, row in data.iterrows()}


def generate_phonetic():
    user_input = input("Type your word: ").upper()
    try:
        final_list = [final_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(final_list)

generate_phonetic()