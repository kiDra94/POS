import urllib.request

url = "https://study.find-santa.eu/data/py/fc.txt"
file_path = "fc.txt"
urllib.request.urlretrieve(url, file_path)

with open(file_path) as f:
    file_content = f.readlines()
    help = []
    x = 0
    avg_count = 0
    for i in file_content:
        if "Saturday" in i or "Sunday" in i:
           help.append(i.split(": "))
    for i in help:
        sum = x + int(i[1])
        x = sum
        avg_count += 1
    temperatur = sum / avg_count

if temperatur > 25:
    activity = "swimming"
elif temperatur > 12:
    activity = "hiking"
elif temperatur > 5:
    activity = "watching movies"
elif temperatur > -5:
    activity = "relaxing in the local hot springs"
else:
    activity = "skiing"
print(f"Next weekend, {activity} would be a good activity.")
    