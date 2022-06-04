from __future__ import absolute_import

from typing import FrozenSet

import graphviz

from graph.router_node import RouterNode
from painter.graph_facade import GraphFacade


class GraphVizPainter:
    def __init__(self, graph: FrozenSet[RouterNode]):
        self.facade = GraphFacade(graph)

    def paint(self):
        nodes_router = self.facade.get_nodes_router()
        nodes_network = self.facade.get_nodes_networks()
        edges = self.facade.get_edges()
        graph = graphviz.Graph('ER', filename='router-analysis.gv', engine='neato')

        graph.attr('node', shape='cylinder')
        for node in nodes_router:
            graph.node(node, label=node)
        graph.attr('node', shape='rectangle')
        for node in nodes_network:
            graph.node(node, label=node)

        # future implementation: show the .x of the network with the label="x'
        for edge in edges:
            graph.edge(edge.router, edge.network, label=edge.ip_host, len='3.00')
        graph.attr(label=r'\n\nYour analysis:\n')
        graph.attr(fontsize='20')
        graph.view()
