# Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys

import csv

def readCsv(filename):
    lst = []
    lstdict = []
    filedict = {}
    with open(filename,'r') as file:
        reader=csv.reader(file)
        for eachline in reader:
            lst.append(eachline)
    name = lst[0][0]
    address = lst[0][1]
    age = lst[0][2]
    for i in range(1, len(lst)):
        filedict[name] = lst[i][0]
        filedict[address] = lst[i][1]
        filedict[age] = lst[i][2]
        lstdict.append(filedict)
        
    print(lstdict)

readCsv('new.csv')
        