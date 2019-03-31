# dials.py
"""
Class Node for creating decision trees.

Each node has a user-defined importance factor (0.0->1.0) and there is a user-defined
function for each output with a user-defined dial setting that together determines
how much of the input goes to each output.
"""
from math import cos, pi


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
  