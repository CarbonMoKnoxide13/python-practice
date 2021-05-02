import time
import os
import requests

# Reads the value stored in dataStorage.txt, if such a value exists
def readValue():
    fr = open("dataStorage.txt", "r")
    time = fr.read()
    fr.close()
    print(time)
    return time

# Writes a given value to dataStorage.txt - if dataStorage.txt doesn't yet exist, the file is created then written to.
def storeValue(value):
    fo = open("dataStorage.txt", "w")
    fo.flush()
    fo.write(str(value))
    fo.close()

# Fetches the current GMT time from the internet
def getCurrentGMTTime():
    try:
        res = requests.get('http://just-the-time.appspot.com/')
        return res.content
    except:
        print('Could not sync with time server.')

    print('Done.')

# Converts the fetched GMT time to PST
def getCurrentPSTTime():
    gmtTime = getCurrentGMTTime()
    splitDateTime = str(gmtTime).split(' ')
    splitTime = splitDateTime[1].split(":")
    hours = int(splitTime[0])
    hours -= 7
    pst = splitDateTime[0] + " " + str(hours) + ":" + splitTime[1] + ":" + splitTime[2]
    pst = pst[2:]
    return pst

# Get the current PST time and write it to dataStorage.txt
pst = getCurrentPSTTime()
storeValue(pst)
readValue()