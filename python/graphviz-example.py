#!/usr/bin/env python3
"""
A simple example to create a graphviz dot file and draw a graph.
"""

import pygraphviz as pgv
from PIL import Image

A = pgv.AGraph()

A.add_edge(1, 2)
A.add_edge(2, 3)
A.add_edge(1, 3)

print(A.string())
print("Wrote simple.dot")
A.write('simple.dot')

B = pgv.AGraph('simple.dot')
B.layout()
B.draw('simple.png')
print("Wrote simple.png")

with Image.open('simple.png') as img:
    img.show()
