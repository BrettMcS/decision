# test_dials.py

import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.insert(0, '..\\decision')

import dials


def plot1():

    xs = np.arange(-0.1, 1.1, 0.02)

    yl = np.array([dials.duo_dial_low(x) for x in xs])
    yh = np.array([dials.duo_dial_high(x) for x in xs])

    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(xs, yl, label="duo dial low")
    ax.plot(xs, yh, label="duo dial high")
    plt.grid()
    plt.legend()
    plt.title("Duo-Dial Output")
    ax.set_xlabel("Dial Setting")
    ax.set_ylabel("Dial Output")
    

def plot2():

    xs = np.arange(-0.1, 1.1, 0.02)

    yl = np.array([dials.tri_dial_low(x) for x in xs])
    yh = np.array([dials.tri_dial_high(x) for x in xs])
    ym = np.array([dials.tri_dial_mid(x) for x in xs])

    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(xs, yl, label="tri dial low")
    ax.plot(xs, yh, label="tri dial high")
    ax.plot(xs, ym, label="tri dial mid")
    plt.grid()
    plt.legend()
    plt.title("Tri-Dial Output")
    ax.set_xlabel("Dial Setting")
    ax.set_ylabel("Dial Output")


if __name__ == "__main__":

    plot1()
    plot2()
    plt.show()