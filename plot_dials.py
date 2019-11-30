# plot _dials.py

import matplotlib.pyplot as plt
import numpy as np

import dials


def test1():

    xs = np.arange(-0.1, 1.1, 0.02)

    yl = np.array([dials.duo_dial_low(x) for x in xs])
    plt.plot(xs, yl, label="duo dial low")

    yh = np.array([dials.duo_dial_high(x) for x in xs])
    plt.plot(xs, yh, label="duo dial high")


def test2():

    xs = np.arange(-0.1, 1.1, 0.02)

    yl = np.array([dials.tri_dial_low(x) for x in xs])
    plt.plot(xs, yl, label="tri dial low")

    yh = np.array([dials.tri_dial_high(x) for x in xs])
    plt.plot(xs, yh, label="tri dial high")

    yh = np.array([dials.tri_dial_mid(x) for x in xs])
    plt.plot(xs, yh, label="tri dial mid")
