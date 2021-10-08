#parser and processing file for lab0
#take the raw data and parse it to just a database of the numbers
#then take the parsed data and process it to calculate and output the slope

import re
import readFile as rf
from collections import namedtuple



#initial lists for raw data
carbData = []
tempData = []

#store raw data into empty lists
carbon = rf.carbonFile(carbData)
temp = rf.tempFile(tempData)


parsedCarbData = {} #initialize empty c02 dictioary with parsed data

#c02 data parser
#sifts through the list of strings from raw data and filters out the numbers i need from each line
#then places the two numbers in their respective values 
for x in range(0, len(carbon.carbonLines) - 12, 12): #this counts by 12 as i only need the year once
    key = re.search("[0-9]{4}", carbon.carbonLines[x]).group()
    #searches for exactly the sequence the "average" value would show up on
    avg = float(0)
    for i in range(x, x + 12):
        #first stored as a string value 
        valStr = re.search("[>]([-]|[0-9])[0-9]{2}[.][0-9]+", carbon.carbonLines[i]).group() 
        valStr = valStr.replace('>', '') #removes the > since we dont need it after searching
        avg = avg + float(valStr)
    avg = avg / 12 #divides it to get the average of that year
    parsedCarbData[int(key)] = avg #store year and average into a dict


parsedTempData = {} #initialize empty temperature dictionray with parsed data

#temperature data parser
#goes through the entire list of lines from the raw data and parses out just the year and the median temperature
for x in range(len(temp.tempLines)):
    key = re.search("[0-9]{4}", temp.tempLines[x]).group()
    val = re.search(".[0-9][.][0-9]+", temp.tempLines[x]).group()
    val = val.replace('>', '') #removes the > if there isn't a '-' symbol preseent thus making the value positive
    parsedTempData[int(key)] = float(val) #assigns the parsed numbers into the temp dictionary as integers and floats


varTup = namedtuple('Database', 'Co2 Temperature') #named tuple that can store the year, co2 and temp values in one database
database = []
carbVal = []
tempVal = []
carbTemp = []
carbSquared = []
for i in range(1959, 2019):
    database.append(varTup(parsedCarbData[i], parsedTempData[i]))
    carbVal.append(parsedCarbData[i])
    tempVal.append(parsedTempData[i])
for i in range(60):
    carbTemp.append(carbVal[i] * tempVal[i])
    carbSquared.append(carbVal[i] * carbVal[i])

slope = (60 * (sum(carbTemp)) - (sum(carbVal)*(sum(tempVal)))) / (60 * sum(carbSquared) - (sum(carbVal) * sum(carbVal)))

#final output hooray!
print(slope)

