"""System test for decision.py"""

import sys

from numpy.random import randn
from numpy import meshgrid

import decision
import dials


if __name__ == "__main__":

    ####################################################################
    #                    CREATE THE DECISION TREE                      #
    ####################################################################
    # Possible outcomes:
    none = decision.Result("No action")
    fea = decision.Result("FEA only")
    stat = decision.Result("FEA & Static Test")
    test = decision.Result("FEA & In-service Test")
    alct = decision.Result("FEA, ALCT & in-service test")

    results = [none, fea, stat, test, alct]

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

    nodes = [precedence, quantity1, load1, quantity2]

    ####################################################################
    #                    SET THE PARAMETERS FOR A RUN                  #
    ####################################################################

    noises = randn(10, 3) * 0.05
    sys.stdout.write("  None  FEA   Test  ALCT\n")

    for noise in noises:

        decision.clear_nodes(results + nodes)

        precedence_dial = 0.5 + noise[0]
        load_factor_dial = 0.6 + noise[1]
        quantity_factor_dial = 0.8 + noise[2]

        precedence.set_dial(precedence_dial)       
        load1.set_dial(load_factor_dial)
        quantity1.set_dial(quantity_factor_dial)       
        quantity2.set_dial(quantity_factor_dial)       

        precedence.activate()

        # print("\nNode imputs:")
        # for node in nodes:
        #     print(f"Node: {node} input is: {node.total_input:.3f}")

        # print("\nResult inputs:")
        # total_inputs = 0.0
        # for result in results:
        #     result_input = result.total_input
        #     total_inputs += result_input
        #     print(f"Result: {result} input is: {result_input:.3f}")
        # print(f"Total result inputs: {total_inputs:.3f}")
        for result in results:
            sys.stdout.write(f"{result.total_input:6.3f}")
        sys.stdout.write('\n')
