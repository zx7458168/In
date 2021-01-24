import math
import time
import json

maxSize = 20
list = {}

def saveToJson():
    data2 = json.dumps(list)
    f = open("json.txt", 'w')
    f.write(data2)
    f.close()

def get(key):
    if (key in list):
        # refresh last access time
        list[key][2] = time.time()
        saveToJson()
        return list[key]
    else:
        return -1

def put(key, value, weight=0):
    # if maxsize is reached, replace it
    key = str(key)
    if (len(list) >= maxSize):
        lowestKey = findLowestItem()
        del list[lowestKey]
        list[key] = [value, weight, time.time()]
    else:
        list[key] = [value, weight, time.time()]
    saveToJson()

# find item with lowest value, return the key of that item
def findLowestItem():
    # get first key and item
    key = next(iter(list))
    low = getScore(list[key][1], list[key][2])
    # find item with lowest value
    for k, v in list.items():
        score = getScore(v[1], v[2])
        if low > score:
            low = score
            key = k
    return key

def getScore(w, lastAccessTime):
    return w / math.log(int(time.time()*1000) - int(lastAccessTime*1000)) if lastAccessTime != time.time() else w / -100
