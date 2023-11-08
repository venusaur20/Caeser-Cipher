mode = input("Decrypt or Encrypt? ")
message = list(input("What would you like to encrypt? "))
shift = int(input("What is your Key? "))
new_message = []

if mode == "decrypt":
    for letter in message:
        if letter == "a": new_message.append(1)
        if letter == "b": new_message.append(2)
        if letter == "c": new_message.append(3)
        if letter == "d": new_message.append(4)
        if letter == "e": new_message.append(5)
        if letter == "f": new_message.append(6)
        if letter == "g": new_message.append(7)
        if letter == "h": new_message.append(8)
        if letter == "i": new_message.append(9)
        if letter == "j": new_message.append(10)
        if letter == "k": new_message.append(11)
        if letter == "l": new_message.append(12)
        if letter == "m": new_message.append(13)
        if letter == "n": new_message.append(14)
        if letter == "o": new_message.append(15)
        if letter == "p": new_message.append(16)
        if letter == "q": new_message.append(17)
        if letter == "r": new_message.append(18)
        if letter == "s": new_message.append(19)
        if letter == "t": new_message.append(20)
        if letter == "u": new_message.append(21)
        if letter == "v": new_message.append(22)
        if letter == "w": new_message.append(23)
        if letter == "x": new_message.append(24)
        if letter == "y": new_message.append(25)
        if letter == "z": new_message.append(26)

def mixer(new_message,shift):
    for letter in range(0,len(new_message)):
        new_message[letter] += shift
    return message


if mode == "encrypt":
        for letter in message:
        if letter == "a": new_message.append(1)
        if letter == "b": new_message.append(2)
        if letter == "c": new_message.append(3)
        if letter == "d": new_message.append(4)
        if letter == "e": new_message.append(5)
        if letter == "f": new_message.append(6)
        if letter == "g": new_message.append(7)
        if letter == "h": new_message.append(8)
        if letter == "i": new_message.append(9)
        if letter == "j": new_message.append(10)
        if letter == "k": new_message.append(11)
        if letter == "l": new_message.append(12)
        if letter == "m": new_message.append(13)
        if letter == "n": new_message.append(14)
        if letter == "o": new_message.append(15)
        if letter == "p": new_message.append(16)
        if letter == "q": new_message.append(17)
        if letter == "r": new_message.append(18)
        if letter == "s": new_message.append(19)
        if letter == "t": new_message.append(20)
        if letter == "u": new_message.append(21)
        if letter == "v": new_message.append(22)
        if letter == "w": new_message.append(23)
        if letter == "x": new_message.append(24)
        if letter == "y": new_message.append(25)
        if letter == "z": new_message.append(26)
#    message == new_message
#    new_message == []

    print(mixer(new_message,shift))
