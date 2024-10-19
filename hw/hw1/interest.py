interest = float(input("Enter interest: "))
amount = float(input("Enter amount: "))
years = int(input("Enter year: "))
amount_print = amount

for i in range(years):
    value = (interest/100) * amount + amount
    amount = value

earned = value - amount_print
print(f"earned {earned:.2f}")
print(f"value {value:.2f}")