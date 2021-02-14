#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
See which graph library is best for my purposes...
https://www.python-course.eu/networkx.php
"""

import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image

G = nx.Graph()
G.add_node("a", time=1)
G.add_nodes_from(["b", "c"], time=3)

G.add_edge(1, 2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw(G)
filename = "simple_path.png"
plt.savefig(filename)  # save as png

with Image.open(filename) as img:
    img.show()
