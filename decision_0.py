# decision.py
"""
Classes for creating decision trees.

Each node has a user-defined importance factor (0.0->1.0) and there is a user-defined
function for each output with a user-defined dial setting that together determines
how much of the input goes to each output.
"""
import numpy as np


class Result:

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

    def __init__(self, title, importance=1.0):
        self.title = title
        self.importance = importance
        self.sub_nodes = []
        self.total_input = 0.0
        self.total_outputs = []
        self.weighters = []
        self.output_weights = []
        self.dial = None

    def __str__(self):
        return self.title

    def attach_sub_node(self, sub_node, output_weighter):
        self.sub_nodes.append(sub_node)
        self.total_outputs.append(0.0)
        self.weighters.append(output_weighter)

    def clear_node(self):
        self.total_input = 0.0
        self.total_outputs = [0.0] * len(self.total_outputs)

    def set_importance(self, importance):
        self.importance = importance

    def set_dial(self, dial):
        self.dial = dial
        self.total_outputs = np.array(self.total_outputs)
        self.output_weights = np.array([wtr(dial) for wtr in self.weighters])

    def activate(self, input_value):
        outputs = input_value * self.importance * self.output_weights
        for output, sub_node in zip(outputs, self.sub_nodes):
            sub_node.activate(output)
        self.total_input += input_value
        self.total_outputs += outputs


class DecisionTree:

    def __init__(self, result_nodes, decision_nodes, title):
        self.title = title
        self.result_nodes = result_nodes
        self.decision_nodes = decision_nodes

    