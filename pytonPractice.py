import time
import os
import requests

def readTime():
    fr = open("dataStorage.txt", "r")
    time = fr.read()
    fr.close()
    print(time)
    return time


def storeTime(time):
    fo = open("dataStorage.txt", "w")
    fo.flush()
    fo.write(str(time))
    fo.close()

def getCurrentGMTTime():
    try:
        res = requests.get('http://just-the-time.appspot.com/')
        return res.content
    except:
        print('Could not sync with time server.')

    print('Done.')

def getCurrentPSTTime():
    gmtTime = getCurrentGMTTime()
    splitDateTime = str(gmtTime).split(' ')
    splitTime = splitDateTime[1].split(":")
    hours = int(splitTime[0])
    hours -= 7
    pst = splitDateTime[0] + " " + str(hours) + ":" + splitTime[1] + ":" + splitTime[2]
    pst = pst[2:]
    return pst

pst = getCurrentPSTTime()
storeTime(pst)
readTime()