
# Read from a CSV file

# arg[1] = file path
# arg[2] = ERD to filter



#TODO: Write to a new CSV without the extra data

import csv
import ast
import sys
from datetime import datetime
#import matplotlib.pyplot as plt 


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y_%S")

#open log file
if len(sys.argv) == 2:
    #use the specified file
    inputFile = sys.argv[1] 
    filterBy = []
    print("sys arg == 2")
    print("sys arg0: "+ sys.argv[0])
    print("sys arg1: "+ sys.argv[1]) 
elif len(sys.argv) == 3:
    #use the specified file
    inputFile = sys.argv[1] 
    #only display the given ERD
    filterBy = sys.argv[2]
    print("sys arg == 3")
    print("sys arg0: "+ sys.argv[0])
    print("sys arg1: "+ sys.argv[1]) 
    print("sys arg2: "+ sys.argv[2]) 
else:
    inputFile = 'CoolingFan_selfClean_2022-02-25T13-14-22.545_1.csv'
    filterBy = []
    print("This is a default --- You may want to input the file you want as an arg ---")
  

file = open(inputFile)

# Get inputs
print()
print("What platform are you using? RC17, OBC1, Striker")
platform = str(input().lower())
print()
print("What size data are you reading (in bytes), only accepts 2 bytes right now")
numberOfBytes = input()


csvreader = csv.reader(file)

if csvreader :
    print("file read successful")
else:
    print("file read NOT successful")

print()

print("Time Stamp                   ERD Sent       ERD Response")

headers = ["Time Stamp", "ERD", "Response"]
rows = []
parsedRows = []
timeStamp = []
sentErd = []
fileName = ""
RX = 0
TX = 0


for row in csvreader:
    #add the row to array
    rows.append(row)

    if ((row[1] == "RX") and (len(row) == 14)):
        # count number of RXs (responses)
        RX = RX + 1
        #only print timestamp, sent ERD, and response
        #strip 0x from item

        if ( (platform == "obc1") or (platform =="obc2") ) :
            if (numberOfBytes == 2):
                newArr = [row[9].replace("0x", ""), row[10].replace("0x", ""), row[12], row[13].replace("0x", "")]
            else:
                print("Cannot proccess anything other than 2 bytes at this time")
        elif (platform == "rc17") :
            if (numberOfBytes == 2):
                newArr = [row[8].replace("0x", ""), row[9].replace("0x", ""), row[12], row[13].replace("0x", "")]
            else:
                print("Cannot proccess anything other than 2 bytes at this time")
        else :
            newArr = []
            print("Program only supports RC17 and OBC platforms")
        
        #join strings together
        timeStamp = row[0]
        sentErd = newArr[0]+newArr[1]
        rawErdResponse = newArr[2]+newArr[3]
        
        #convert ERD response from hex to decimal
        parsedErd = str(int(rawErdResponse, 16))

        #print to console
        print(timeStamp + "\t\t" + sentErd + "\t\t" + parsedErd)
        
        #write to file
        fileName = "./Results/parsedResults"+ dt_string +".csv"
        
        #add items to array
        parsedRow = [timeStamp, sentErd, parsedErd]
        parsedRows.append(parsedRow)
        
    else:
        #print("TX")
        TX = TX + 1
        
#print(parsedRows)
print ("")
print("File to read: " + inputFile)

with open(fileName, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)
        
    # writing the fields 
    csvwriter.writerow(headers) 
    
    # writing the data rows 
    csvwriter.writerows(parsedRows)
    print("File created: " + fileName)

# Calculate percentage of sent messages compared to recieved
percentRxTx = (1 - (RX / TX)) * 100

print ("")

#print("Percentage of data lost")
print(str(round(percentRxTx)) + "% of data lost")
print ("")

print("END...")

#Draw the line graph
#plt.plot(timeStamp,parsedErd)
#plt.title('title name')
#plt.xlabel('Time')
#plt.ylabel('sentErd[0]')
#plt.show()
file.close()