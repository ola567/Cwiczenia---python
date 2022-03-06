import sys

def find_indexes(w, l):
    indexes=[]
    for index, letter_in_word in enumerate(word):
        if l == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game(triess):
    print()
    print(user_word)
    print("Pozostalo "+ str(triess)+ " prób.")
    print("Użyte litery: ", used_letters)
    print()

tries = 5
word="kamila"
user_word = []
used_letters = []

for _ in word:
    user_word.append("_")

while True:
    letter=input("Podaj literę: ")
    used_letters.append(letter)
    found_indexes=find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        tries -=1
        if tries ==0:
            print("Koniec gry")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        print(user_word)

        if "".join(user_word) == word:
            print("Wygrałeś!!")
            sys.exit(0)
            
    show_state_of_game(tries)