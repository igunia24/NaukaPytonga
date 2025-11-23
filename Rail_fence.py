#!/usr/bin/env

def rail_fence_encrypt(text, rails):
    """Rail Fence encryprion

    Takes:
    text: str - text to encrypt
    rails: int - number of rails

    Returns:
    str - encrypted text
    """
    #Text prep
    text = text.upper().strip().split(" ")
    text_strp = "".join(text)
    #Blank rails
    rails_dict = {rail: [] for rail in range(rails)}

    num = 0
    row = 0
    direction = 1   #1 - down, -1 - up
    while num < len(text_strp):
        letter = text_strp[num]
        rails_dict[row].append(letter)   #add letter

        #zmiana kierunku
        if row == (rails - 1):
            direction = -1
        elif row == 0:
            direction = 1

        num += 1
        row += direction

    #łączenie szyn w zaszyfrowany tekst
    encrypted_text = []
    for value in rails_dict.values():
        encrypted_text += value

    return("".join(encrypted_text))   #zwraca zaszyfrowany tekst

def rail_fence_decrypt(text, rails):
    """Rail Fence decryption

    Takex:
    text: str - encrypted text
    rails: int - number of rails

    Returns:
    str - decrypted text w/o spaces"""

    rails_dict = {rail: [] for rail in range(rails)}
    num = 0
    row = 0
    direction = 1

    #finding letter numbers for each rail
    while num < len(text):
        rails_dict[row].append(num)
        if row == (rails - 1):
            direction = -1
        elif row == 0:
            direction = 1
        num += 1
        row += direction

    #preparation of letters order
    letter_order = []
    for value in rails_dict.values():
        letter_order += value

    #putting letters in the "right" order
    decrypted = [""] * len(text)
    for pos, letter in zip(letter_order, text):
        decrypted[pos] = letter

    return "".join(decrypted)


message = input("What message do you want to encrypt: ")  #pobiera od użytkownika tekst

#takes and proofs rails number
while True:
    try:
        num_rails = int(input("Number of rails: "))
        if num_rails > 1:
            break
        print("Rails number must be >1.")
    except ValueError:
        print("Error! Must be an integer.")

#encryption
encrypted = rail_fence_encrypt(message, num_rails)

#result for the user
print(f"Your text: {message}")
print(f"Rails: {num_rails}")
print(f"Encrypted text: {encrypted}")

while True:
    to_decrypt = input("Do you and to decrypt ypur message? [Y - yes/n- no] ")
    if to_decrypt == "Y":
        decrypted_message = rail_fence_decrypt(encrypted, num_rails)
        print(f"Decrypted message: {decrypted_message}")
        break
    elif to_decrypt == "n":
        print("Ok! Good bye!")
        break
    else:
        print("Error! Please choose Y (to decrypt) or n (to finish programm).")
print("Sorry, you have to separate words yourself. Enjoy!")
