user = int(input("Integer: "))
results = []
factor = 2
print(f"{user} = ", end="")
while user >= 2:
    if user%factor == 0:
        results.append(factor)
        user /= factor
    else:
        factor += 1
for i in results:
    if i <= len(results):
        print(f"{i} * ", end="")
    else:
        print(f"{i}")