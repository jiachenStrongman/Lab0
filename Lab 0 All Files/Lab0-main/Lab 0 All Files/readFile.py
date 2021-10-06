#Lab 0 taking in the file data
#this file just opens the html files to store whatever data is inside

class carbonFile:

    def __init__(self, carbonLines): #initialize carbonfile obj method
        self.carbonLines = carbonLines
        #opens the co2.html file and stores each line into an object called carbonLines
        carbon = open('Co2.html', 'r')
        self.carbonLines = carbon.readlines()
        for i in range (4):
            del self.carbonLines[i]
        #removes first 3 lines that have no use in the program

class tempFile:
    
    def __init__(self, tempLines):
        self.tempLines = tempLines
        #opens the temprature.html file and stores each line to the tempLines list
        temp = open('Temperature.html', 'r')
        self.tempLines = temp.readlines()
        for i in range(5):
            del self.tempLines[i]
        #removes the first 4 lines in the file as they have no use in this program
