import csv
data1 = []
data2 = []

with open("final.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data1.append(i)

with open("archive_dataset.csv","r") as f:
    csv_reader= csv.reader(f)
    for i in csv_reader:
        data2.append(i)

header_1 = data1[0]
planet_data_1 = data1[1:]
header_2 = data2[0]
planet_data_2 = data2[1:]

header = header_1+header_2
planet_data=[]
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("merged.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(planet_data)
