#Lab 0 taking in the file data
#this file just opens the html files to store whatever data is inside

class carbonFile:

    def __init__(self, carbonLines): #initialize carbonfile obj method
        #opens the co2.html file and stores each line into an object called carbonLines
        carbon = open('Co2.html', 'r')
        self.carbonLines = carbon.readlines()
        #self.carbonLines = carbon.readlines()
        for i in range(4):
            del self.carbonLines[0]
        #removes first 3 lines that have no use in the program
        del self.carbonLines[-1]
        #removes end </table> tag on the last line since i wont need it

class tempFile:
    
    def __init__(self, tempLines):
        #opens the temprature.html file and stores each line to the tempLines list
        temp = open('Temperature.html', 'r')
        self.tempLines = temp.readlines()
        for i in range(5):
            del self.tempLines[0]
        #removes the first 4 lines in the file as they have no use in this program
        del self.tempLines[-1]
        #removes end </table> tag on the last line as i wont need it in this program

#this is a test to make sure the raw file is stored properly i just have it print a random element/line
#in the data to see if it retrieved the right one
#carb = carbonFile([])
#print(carb.carbonLines[0])
#for i in range(5):
 #   print(carb.carbonLines[i])
#temp = tempFile([])
#print(temp.tempLines[-1])
