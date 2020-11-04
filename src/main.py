#!/usr/bin/env python3

#import Adafruit_DHT
import datetime
import matplotlib.pyplot as plt
import numpy as np

#sensor = Adafruit_DHT.AM2302
pin = 4

def get_temp_humidity():
    result  = False
    while(result != True):
        #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # temperature = temperature * 9/5.0 + 32 #Farenheit

        if humidity is not None and temperature is not None:
            result = True
        else:
            result = False
    return [round(temperature,1),round(humidity,1)]

def get_temperature(sauvegardeStatus):
    tmp = 0
    for i in range(5):
        tmp += get_temp_humidity()[0]
    if(sauvegardeStatus):
        enregistrement(round(tmp/5,1))
    return round(tmp/5,1)

def get_humidity():
    tmp = 0
    for i in range(5):
        tmp += get_temp_humidity()[1]
    return round(tmp/5,1)

def enregistrement(temp):
    date = str(datetime.datetime.now())[:-10]
    with open("../data.txt", "a") as fichier:
        fichier.write(str(date) + "," + str(temp) + "\n")