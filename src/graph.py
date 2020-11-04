#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

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

data = fichierVersListe("data/data.txt")

plt.title("Variation de la température et de l'humidité en fonction du temps")
plt.xlabel("Température")
plt.ylabel("Date/heure")
plt.plot(data[0],data[1])

plt.savefig("test.png")