#!/usr/bin/env python3

import Adafruit_DHT
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import time

# fonction et variable de température ---------------------------

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

#----------------------------------------------------------------

# fonction de gestion de fichier --------------------------------

def enregistrement(temperature, mainDir):
    '''Record temperature in the data directory for the 

        Args:
            temperature (float): Temperature to record
            mainDir (str): Path of the application "<Path>/domotic/"

        Raises:
            /

        Returns:
            /
        '''
    date = str(datetime.datetime.now())[:-10]

    if( os.path.isfile(str(mainDir + "data/" + date[:10] + ".txt")) ):
        with open(mainDir + "data/" + date[:10] + ".txt", "a") as fichier:
            fichier.write(date[11:] + "," + str(temperature) + "\n")
    else:
        with open(mainDir + "data/" + date[:10] + ".txt", "w") as fichier:
            fichier.write(date[11:] + "," + str(temperature) + "\n")


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

def data_to_graph(mainDir,date):
    data = fichierVersListe(mainDir + "data/" + str(date) + ".txt")
    plt.plot(data[0],data[1], color='g', label="Température")
    plt.title("Variation de la température en fonction du temps")
    plt.xlabel("Heure")
    plt.ylabel("Température")

    plt.savefig(mainDir + "static/images/test.png")

#----------------------------------------------------------------

# Programme de traitement ---------------------------------------

def program(mainDir):
    date = str(datetime.datetime.now())[:-10]
    temp = get_temperature()
    enregistrement(temp,mainDir)
    data_to_graph(mainDir,date)
    print("saved picture at " + str(datetime.datetime.now())[11:16] + " the " + str(datetime.datetime.now())[:10] + " with temperature of " + str(temp) + "'C\n")

#----------------------------------------------------------------

if __name__ == "__main__":
    main_dir = str(os.path.abspath(__file__))[:-11]
    #os.system(main_dir + "server.py &")

    print("[!] Début du programme\n")
    actual_time = None

    while(True):
        time = int(str(datetime.datetime.now())[14:16])
        if ( time != actual_time ):
            #17:19 : secondes et 14:16 : minutes
            actual_time = int(str(datetime.datetime.now())[14:16])
            program(main_dir)
            
    print("[!] Fin du programme\n")