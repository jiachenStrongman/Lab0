#parser file for lab0
#take the raw data and parse it to just a database of the numbers 

import re
import readFile as rf

carbData = []
tempData = []

carbon = rf.carbonFile(carbData)
temp = rf.tempFile(tempData)


