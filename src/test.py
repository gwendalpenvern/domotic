#!/usr/bin/env python3

import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help="give you some debug information", action="store_true", default=False)
    parser.add_argument('-t', '--timming', help="time interval between every point measure (minute)", default=5)
    args = parser.parse_args()

    return args

print(parser().timming)