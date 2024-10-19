user_file = input("Files: ").split(",")
user_needle = input("Needle: ").lower()

with open(user_file[0]) as f1, open(user_file[1]) as f2:
    file1 = f1.read().lower()
    file2 = f2.read().lower()
    count = file1.count(user_needle) + file2.count(user_needle)
    print(f"Occurrences: {count}")
    