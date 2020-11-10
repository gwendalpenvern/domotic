#!/usr/bin/env python3

import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import argparse

def fichierVersListe(cheminFich):
    f = open(cheminFich, "r")
    temperature = []
    for line in f:
        temperature.append(float(line.split("\n")[0].split(",")[1]))
    f.close()
    return temperature

def get_actual_temperature():
    main_dir = str(os.path.abspath(__file__))[:-11]
    #day = str(datetime.datetime.now())[:10]
    day = "2020-11-05"
    try:
        return fichierVersListe(main_dir + "data/" + day + ".txt")[-1]
    except:
        return "Unknown"

print(get_actual_temperature())