#Lab 0 taking in the file data
#this file just opens the html files to store whatever data is inside

#opens the co2.html file and stores each line into an object called carbonLines
carbonLines = []
with open('Co2.html', 'r') as carbon:
    #this should create the desired list of strings for the carbon files
    carbonLines = carbon.read().splitlines()

tempLines = []
with open('Temperature.html', 'r') as temp:
    tempLines = temp.read().splitlines()

for x in range(0,9):
    print(tempLines[x])
