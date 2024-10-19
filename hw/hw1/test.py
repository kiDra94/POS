user = int(input("One number: "))
for i in range(0, user, 2):
    if i%2==0:
        i = i**2
        if i<user:
            print(f"{i}")
a=0
while a < user:
    if a%2==0:
        b = a**2
        if b > user:
            break
        print(b)
    a += 1
