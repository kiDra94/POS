user = input("File to decode: ")

with open(user) as f:
    rot13 = f.read().upper()
    for char in rot13:
        if ord(char) >= 65 and ord(char) <= 77:
            print(chr(ord(char) + 13), end="")
        elif ord(char) >= 78 and ord(char) <= 90:
            print(chr(ord(char) - 13), end="")
        else:
            print(char, end="")