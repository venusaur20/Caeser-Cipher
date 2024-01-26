mode_choice = input("Decrypt or Encrypt? ").lower

if list(mode_choice)[0] == "d":
    mode = ("decrypt")
elif list(mode_choice)[0] == "e":
    mode = ("encrypt")

message = list(input(f"What would you like to {mode}? ").lower)
shift = int(input("What is your Key? "))

ALPHABET = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}


def Encrypt():
    message_values = []
    for letter in range(len(message)):
        message_values.append(ALPHABET.values(message[letter]))
    
    print(message_values)

def mixer(new_message,shift):
    for letter in range(0,len(new_message)):
        new_message[letter] += shift
    return message


#if mode == "encrypt":
#        for letter in message:

#    message == new_message
#    new_message == []
#
#    print(mixer(new_message,shift))
