# Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for each tuple

import csv

def writeCsv(filename, lst):
    with open(filename,'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['name', 'address', 'age'])
        for row in lst:
            writer.writerow(row)

data=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)]

writeCsv('new.csv', data)

