#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

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

def data_to_graph():
    data = fichierVersListe("data/data.txt")
    plt.title("Variation de la température et de l'humidité en fonction du temps")
    plt.xlabel("Date/heure")
    plt.ylabel("Température")
    plt.plot(data[0],data[1])

    plt.savefig("test.png")