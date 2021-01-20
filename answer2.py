import time
import math

class Data:
    current_time = time.time()
    last_access_time = float(open('saveTime.txt', 'r').readline())
    list = {}
    score = 0

def get(key):
    return Data.list[key] if key in list else -1

def put(key, value, weight=0):
    Data.list[key] = value
    f = open('saveTime.txt','w')
    f.write(str(Data.current_time))
    f.close()
    Data.score = scoreProducer(weight)

def scoreProducer(weight):
    return weight/math.log(Data.current_time - Data.last_access_time) if Data.last_access_time != Data.current_time else weight/-100