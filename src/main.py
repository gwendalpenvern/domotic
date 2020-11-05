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

def get_temperature():
    tmp = 0
    for i in range(5):
        tmp += get_temp_humidity()[0]
    return round(tmp/5,1)

def get_humidity():
    tmp = 0
    for i in range(5):
        tmp += get_temp_humidity()[1]
    return round(tmp/5,1)

def enregistrement(temp, mainDir):
    date = str(datetime.datetime.now())[:-10]
    with open(mainDir + "data/data.txt", "a") as fichier:
        fichier.write(str(date) + "," + str(temp) + "\n")

def fichierVersListe(cheminFich):
    f = open(cheminFich, "r")
    points = []
    temperature = []
    for line in f:
        print()
        points.append(line.split("\n")[0].split(",")[0])
        temperature.append(float(line.split("\n")[0].split(",")[1]))
    f.close()
    return [points, temperature]

def data_to_graph(mainDir):
    data = fichierVersListe(mainDir + "data/data.txt")
    plt.title("Variation de la température et de l'humidité en fonction du temps")
    plt.xlabel("Date/heure")
    plt.ylabel("Température")
    plt.plot(data[0],data[1])

    plt.savefig(mainDir + "static/images/test.png")

def program(mainDir):
    temp = get_temperature()
    enregistrement(temp,mainDir)
    data_to_graph(mainDir)
    print("saved picture at " + str(datetime.datetime.now())[11:16] + " the " + str(datetime.datetime.now())[:10] + " with temperature of " + str(temp) + "\n")



if __name__ == "__main__":
    main_dir = str(os.path.abspath(__file__))[:-11]
    #os.system(main_dir + "server.py &")

    print("[!] Début du programme\n")
    actual_time = None

    while(True):
        if ( int(str(datetime.datetime.now())[14:16]) != actual_time ):
            #17:19 : secondes et 14:16 : minutes
            actual_time = int(str(datetime.datetime.now())[14:16])
            program(main_dir)
            
    print("[!] Fin du programme\n")