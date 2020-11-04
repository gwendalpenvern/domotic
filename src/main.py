#!/usr/bin/env python3

import Adafruit_DHT
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import time

sensor = Adafruit_DHT.AM2302
pin = 4

def get_temp_humidity():
    result  = False
    while(result != True):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
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

def fichierVersListe(cheminFich):
    f = open(cheminFich, "r")
    points = []
    temperatures = []
    for line in f:
        print()
        points.append(line.split("\n")[0].split(",")[0])
        temperature.append(float(line.split("\n")[0].split(",")[1]))
        humidity.append(float(line.split("\n")[0].split(",")[2]))
    f.close()
    return [points, temperature, humidity]



if __name__ == "__main__":
    main_dir = str(os.path.abspath(__file__))[:-11]
    #os.system(main_dir + "server.py &")

    for i in range(15):
        print("in")
        time.sleep(60)
        os.system("curl -s '0.0.0.0:5000' > /dev/null")
    