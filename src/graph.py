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
        temperatures.append(float(line.split("\n")[0].split(",")[1]))
    f.close()
    return [points, temperatures]

data = fichierVersListe("data/data.txt")

plt.title("distance en fonction de la puissance re  ue")
plt.xlabel("distance approximative (metre)")
plt.ylabel("puissance re  ue (dBm)")
plt.plot(data[0],data[1])

plt.savefig("test.png")
