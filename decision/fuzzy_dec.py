# fuzzy_dec.py

import math

from scipy.interpolate import interp1d


class FuzzyNode:

    def __init__(self, name="", initial_value=0.0):
        self.name = name
        self.input_value = initial_value
        self.members = []
        self.targets = []

    def connect(self, member, target_node):
        self.members.append(member)
        self.targets.append(target_node)

    def run(self, input_value):
        print(f"Running node {self.name} with input: {input_value:5.3f}")
        self.input_value += input_value
        for target, member in zip(self.targets, self.members):
            target.run(member.value(self.input_value))


def list_nodes(node):
    yield node
    for target in node.targets:
        yield from list_nodes(target)


class Bell:

    def __init__(self, mean, std_dev):

        self.mean = mean
        self.factor2 = -1.0 / (2.0 * std_dev**2)

    def value(self, x):
        return math.exp(self.factor2 * (x - self.mean)**2)


class Trapezoid:

    def __init__(self, left_base, left_top, right_top, right_base):

        x = np.array([left_base, left_top, right_top, right_base])
        y = np.array([0.0, 1.0, 1.0, 0.0])

        self.value = interp1d(x, y, bound_error=False, fill_value=0.0)


if __name__ == "__main__":

    import numpy as np
    import matplotlib.pyplot as plt

    mem1 = Bell(0.2, 0.1)
    mem2 = Bell(0.5, 0.25)
    mem3 = Bell(0.7, 0.15)

    input_values = np.arange(0.0, 1.0, 0.01)

    values1 = [mem1.value(input_value) for input_value in input_values]
    values2 = [mem2.value(input_value) for input_value in input_values]
    values3 = [mem3.value(input_value) for input_value in input_values]

    plt.plot(input_values, values1, '-o')
    plt.plot(input_values, values2, '-o')
    plt.plot(input_values, values3, '-o')

    nodeA = FuzzyNode("Node A")
    node1 = FuzzyNode("Node 1")
    node2 = FuzzyNode("Node 2")
    node3 = FuzzyNode("Node 3")

    node2a = FuzzyNode("Node 2A")
    node2b = FuzzyNode("Node 2B")
    node2c = FuzzyNode("Node 2C")

    node3a = FuzzyNode("Node 3A")
    node3b = FuzzyNode("Node 3B")
    node3c = FuzzyNode("Node 3C")

    nodeA.connect(mem1, node1)
    nodeA.connect(mem2, node2)
    nodeA.connect(mem3, node3)

    node2.connect(mem2, node2a)
    node2.connect(mem2, node2b)
    node2.connect(mem2, node2c)

    node3.connect(mem1, node3a)
    node3.connect(mem1, node3b)
    node3.connect(mem1, node3c)

    nodeA.run(0.6)

    for node in list_nodes(nodeA):
        print(f"{node.name}: {node.input_value:5.3f}")
