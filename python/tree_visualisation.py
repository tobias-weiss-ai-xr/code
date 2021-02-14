#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" tree visualisation

    stolen from: https://medium.com/@rnbrown/
                        creating-and-visualizing-decision-trees-
                        with-python-f8e8fa394176
"""


import sklearn.datasets as datasets
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
# from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

dtree = DecisionTreeClassifier()
dtree.fit(df, y)

dot_data = StringIO()

export_graphviz(dtree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("dtree.png")
img = mpimg.imread("dtree.png")
imgplot = plt.imshow(img)
plt.show()
