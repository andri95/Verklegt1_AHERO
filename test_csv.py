import csv

csv_file = open('Crew.csv', 'r')
csv_reader = csv.reader(csv_file)

next(csv_reader)  #  Skippar t.d Licence efsta dótið

for line in csv_reader:
    if line[0] == '2209955782':
        line[8] += '\FokkarF28'
    print(line[8])



#William Carillo