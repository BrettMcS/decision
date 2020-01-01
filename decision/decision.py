# decision.py
"""
Classes for creating and running decision trees.

Each node has a user-defined importance factor (0.0->1.0) and there is a
user-defined function for each output with a user-defined dial setting
that together determines how much of the input goes to each output.
"""
import numpy as np


class Result:
    """
    A node that accumulates the outputs of nodes connected to it.
    """
    def __init__(self, title):
        self.title = title
        self.total_input = 0.0

    def __str__(self):
        return self.title

    def clear_node(self):
        self.total_input = 0.0

    def activate(self, input_value):
        self.total_input += input_value


class Node:
    """
    A node that parcels its input into multiple outputs, also accumlating
    the inputs.
    """
    def __init__(self, title):
        self.title = title
        self.sub_nodes = []
        self.total_input = 0.0
        self.total_outputs = []
        self.weighters = []
        self.output_weights = []
        self.dial_setting = 0.5

    def __str__(self):
        return self.title

    def attach_sub_node(self, sub_node, output_weighter):
        self.sub_nodes.append(sub_node)
        self.total_outputs.append(0.0)
        self.weighters.append(output_weighter)

    def clear_node(self):
        self.total_input = 0.0
        self.total_outputs = [0.0] * len(self.total_outputs)

    def set_dial(self, dial):
        self.dial_setting = dial
        self.output_weights = np.array([wtr(dial) for wtr in self.weighters])

    def activate(self, input_value):
        if self.sub_nodes:
            outputs = input_value * self.output_weights
            for output, sub_node in zip(outputs, self.sub_nodes):
                sub_node.activate(output)
            self.total_outputs = list(np.array(self.total_outputs) + outputs)
        self.total_input += input_value


def clear_nodes(nodes):
    for node in nodes.values():
        node.clear_node()
