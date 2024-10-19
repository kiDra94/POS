user = float(input("Enter a distance in meters: "))
inch = user*100 / 2.54
feet = inch / 12
yard = feet / 3
mile = yard / 1760
print(f"{inch:.2f} inch\n{feet:.2f} feet\n{yard:.2f} yards\n{mile:.2f} miles")