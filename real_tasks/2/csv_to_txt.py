import csv

data = []

with open("./rr.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        val = row[0].strip()
        try:
            data.append(str(int(val)))
        except:
            continue
    
with open("./rr.txt", "w") as txt_file:
    text = "\n".join(data)
    txt_file.write(text)