"""System test for decision.py"""

from decision import Node, Result
import dials


def test_1():

    node1 = Node("node1")
    node1.set_dial(0.5)
    node1.activate(1.0)

    assert node1.total_input == 1.0


def test_2():

    node1 = Node("node1")
    node2 = Node("node2")

    node1.attach_sub_node(node2, dials.duo_dial_low)

    node1.set_dial(0.5)
    node1.activate(0.5)

    assert node2.total_input == 0.25

