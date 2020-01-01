# Decision-Making Flowchart Tool

A module for helping to make decisions using a flow chart

There are decision nodes and result nodes. Each decision nodes has 2
or 3 outputs which will weight (multiply) the input value to the
decision node and apply it to the output.

The result nodes represent decisions. They just accumulate their inputs.
The idea is that theresult node with the largest accumalated input
represents the 'best' decision.

At the moment this is just programmatic, to check that it is working.
A proper implementation would have graphical construction of the
flow chart and the results.