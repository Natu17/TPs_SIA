import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

net = nx.DiGraph()
def update(node):
    #net.add_node(node)
    #net.add_node(node.parent)
    net.add_edge(node.parent,node,label = node.action)
    pos = graphviz_layout(net, prog="dot")
    plt.clf()
    nx.draw(net,pos)
    edges = nx.get_edge_attributes(net, "label")
    nx.draw_networkx_edge_labels(net,pos,edges)
    plt.draw()
    plt.pause(0.001)
plt.ion()