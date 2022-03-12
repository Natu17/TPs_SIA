import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

net = nx.DiGraph()
def update(node):
    #net.add_node(node)
    #net.add_node(node.parent)
    net.add_edge(node.parent,node)
    pos = graphviz_layout(net, prog="dot")
    plt.clf()
    nx.draw(net,pos)
    plt.draw()
    plt.pause(0.001)
plt.ion()