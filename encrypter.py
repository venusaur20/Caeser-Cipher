mode_choice = input("Decrypt or Encrypt? ").upper()

if "N" in mode_choice:
    mode = ("encrypt")
elif "D" in mode_choice:
    mode = ("decrypt")

message = list(input(f"What would you like to {mode}? ").lower())


ALPHABET = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}


def crypt():
    message_values = []
    for letter in range(len(message)):
        corresponding_value = message[letter]
        if corresponding_value != " ":
            message_values.append(ALPHABET[corresponding_value])
        else:
            message_values.append(" ")
    
    return message_values

def mix(message_values,shift):
    mixed_values = []
    mixed_message = []

    for letter in range(len(message_values)):
        mixed_values.append(shift+(message_values[letter]))

    for letter in range(len(mixed_values)):
        corresponding_word = mixed_values[letter]
        mixed_message.append(list(ALPHABET.keys())[corresponding_word-1])

    return(''.join(mixed_message))

def tool():

    if mode == "encrypt":
        shift = int(input("What is your Key? "))

    elif mode == "decrypt":
        shift = (int(input("What is your Key? ")))*(-1)

    message_values = crypt()
    print(mix(message_values,shift))


while True:
    tool()
    again = ("\n Again? ").upper()
    if "Y" in again:
        continue
    else:
        break