"""System test for decision.py"""

import sys
sys.path.insert(0, '..\\decision')

import numpy as np

import decision
import dials


def create_flowchart():

    ####################################################################
    #                    CREATE THE DECISION TREE                      #
    ####################################################################
    # Possible outcomes:
    none = decision.Result("No action")
    fea = decision.Result("FEA only")
    stat = decision.Result("FEA & Static Test")
    test = decision.Result("FEA & In-service Test")
    alct = decision.Result("FEA, ALCT & in-service test")

    # Define and connect the nodes in the tree
    # top node:
    precedence = decision.Node("Design Precedence")

    # next level nodes, ie sub-nodes:
    quantity1 = decision.Node("Quantity of bogies")
    load1 = decision.Node("Load factor cf precedent")

    # attach sub-nodes to top node:
    precedence.attach_sub_node(quantity1, dials.duo_dial_low)
    precedence.attach_sub_node(load1, dials.duo_dial_high)

    # attach result nodes to quantity1 factor node:
    quantity1.attach_sub_node(fea, dials.tri_dial_low)
    quantity1.attach_sub_node(test, dials.tri_dial_mid)
    quantity1.attach_sub_node(alct, dials.tri_dial_high)

    # next level nodes
    quantity2 = decision.Node("Quantity of bogies")

    # attach sub-nodes to load1 factor node:
    load1.attach_sub_node(none, dials.tri_dial_low)
    load1.attach_sub_node(quantity2, dials.tri_dial_mid)
    load1.attach_sub_node(quantity1, dials.tri_dial_high)

    # attach result nodes to quantity2 factor node:
    quantity2.attach_sub_node(none, dials.duo_dial_low)
    quantity2.attach_sub_node(fea, dials.duo_dial_high)

    decision_nodes = dict(precedence=precedence, quantity1=quantity1,
                          load1=load1, quantity2=quantity2)

    result_nodes = dict(none=none, fea=fea, stat=stat, test=test, alct=alct)

    return decision_nodes, result_nodes


def test_1():

    decision_nodes, result_nodes = create_flowchart()

    sys.stdout.write("  None  FEA   In-Service   ALCT  ALCT+In-Service\n")

    decision.clear_nodes(decision_nodes)
    decision.clear_nodes(result_nodes)

    decision_nodes['precedence'].set_dial(0.5)
    decision_nodes['load1'].set_dial(0.6)
    decision_nodes['quantity1'].set_dial(0.8)
    decision_nodes['quantity2'].set_dial(0.8)

    decision_nodes['precedence'].activate(1.0)

    print("\nNode imputs:")
    for node in decision_nodes.values():
        print(f"Node: {node} input is: {node.total_input:.3f}")

    print("\nResult inputs:")
    results = np.array([result.total_input for result in result_nodes.values()])

    total_inputs = np.sum(results)
    for result, node in zip(results, result_nodes.values()):
        print(f"Result: {node} input is: {result:.4f}")

    print(f"Total result inputs: {total_inputs:.3f}")

    for result in result_nodes.values():
        sys.stdout.write(f"{result.total_input:6.3f}")
    sys.stdout.write('\n')

    result_ans = np.array([0.0432, 0.4091, 0.0000, 0.1892, 0.3585])

    print(result_ans - results)

    assert abs(total_inputs - 1.0) < 1.0e-6
    assert np.allclose(results, result_ans, atol=1.0e-3)


# def noisy_run():

    # from numpy.random import randn
    # from numpy import meshgrid

#     nodes, results = create_flowchart()

#     noises = randn(10, 3) * 0.05
#     sys.stdout.write("  None  FEA   In-Service   ALCT  ALCT+In-Service\n")

#     for noise in noises:

#         decision.clear_nodes(results + nodes)

#         precedence_dial = 0.5 + noise[0]
#         load_factor_dial = 0.6 + noise[1]
#         quantity_factor_dial = 0.8 + noise[2]

#         precedence.set_dial(precedence_dial)
#         load1.set_dial(load_factor_dial)
#         quantity1.set_dial(quantity_factor_dial)
#         quantity2.set_dial(quantity_factor_dial)

#         precedence.activate()

#         for result in results:
#             sys.stdout.write(f"{result.total_input:6.3f}")
#         sys.stdout.write('\n')
