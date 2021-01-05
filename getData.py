import csv

def getData(CSV):

    listCSV = []

    with open(CSV) as CSV:

        readCSV = csv.reader(CSV)

        for record in readCSV:
            
            listCSV.append(record)

    return listCSV

def appendRecord(CSV, record):

    with open(CSV, 'a', newline = '') as CSV:
                  
        writeCSV = csv.writer(CSV)

        writeCSV.writerow(record)

def updateTable(CSV, newTable):

    with open(CSV, 'w', newline = '') as CSV:
                      
        writeCSV = csv.writer(CSV)

        for line in newTable:

            writeCSV.writerow(line)
