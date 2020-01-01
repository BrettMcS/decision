# dials.py
"""
Dials. Input the dial setting and get the output from.
"""
from math import cos, pi


#TODO: Look into providing multiple output, ensuring that the total is 1


def duo_dial_low(dial_setting):
    if 0.0 < dial_setting < 1.0:
        return 0.5 * (1.0 + cos(pi*dial_setting))
    else:
        return 0.0

def duo_dial_high(dial_setting):
    if 0.0 < dial_setting < 1.0:
        return 0.5 * (1.0 - cos(pi*dial_setting))
    else:
        return 0.0


def tri_dial_low(dial_setting):
    if 0.0 < dial_setting < 0.5:
        return 0.5 * (1.0 + cos(2*pi*dial_setting))
    else:
        return 0.0

def tri_dial_mid(dial_setting):
    if 0.0 < dial_setting < 1.0:
        return 0.5 * (1.0 - cos(2*pi*dial_setting))
    else:
        return 0.0

def tri_dial_high(dial_setting):
    if 0.5 < dial_setting < 1.0:
        return 0.5 * (1.0 + cos(2*pi*dial_setting))
    else:
        return 0.0
  