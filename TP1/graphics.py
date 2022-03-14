import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

net = nx.DiGraph()
def update(node):
    net.add_node(node, label=node.heuristic)
    #net.add_node(node.parent)
    net.add_edge(node.parent,node,label = node.action)
    pos = graphviz_layout(net, prog="dot")
    plt.clf()
    nx.draw(net,pos, node_size=1000, node_color="black")
    edges = nx.get_edge_attributes(net, "label")
    nodes = nx.get_node_attributes(net, "label")
    nx.draw_networkx_edge_labels(net,pos,edges)
    nx.draw_networkx_labels(net,pos, nodes, font_color="white")
    plt.draw()
    plt.pause(0.001)
plt.ion()