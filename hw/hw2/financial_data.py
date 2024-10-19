
with open("ANDR.VI.csv") as f:
    files = []
    avg_helper = 0
    counter = 0
    for row in f:
        files.append(row.split(","))
    for index, word in enumerate(files[0]):
        if word == "Close":
            close = index
    for index, word in enumerate(files):
        if index >= 1:
            sum = float(files[index][close]) + avg_helper
            avg_helper = sum
            counter += 1
    avg = sum/counter
    print(f"File to analyze: The average closing price was {avg:.2f}.")
    if float(files[counter][close]) < avg:
        print(f"The most recent closing price ({float(files[counter][close])}) was not above the average.")
    elif float(files[counter][close]) > avg:
        print(f"The most recent closing price ({float(files[counter][close])}) was above the average.")
    else:
        print(f"The most recent closing price ({float(files[counter][close])}) was equal the average.")