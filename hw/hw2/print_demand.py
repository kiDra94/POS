import urllib.request

url = "https://study.find-santa.eu/data/py/r101.txt"
file_path = "r101.txt"

urllib.request.urlretrieve(url, file_path)

with open(file_path) as f:
    help = []
    column = 0
    avg_help = 0
    for row in f:
        help.append(row.split("."))
    for index, word in enumerate(help[0]):
        if "DEMAND" in word:
            column = index
    for index, value in enumerate(help):
        if index > 0:
            total_demand = int(value[column-1].replace(" ", "0")) + avg_help
            avg_help = total_demand
print(f"Total demand: {total_demand:.1f}")
            

        
    
