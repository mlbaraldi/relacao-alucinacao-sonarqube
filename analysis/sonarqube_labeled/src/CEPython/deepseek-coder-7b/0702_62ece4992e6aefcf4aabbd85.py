from rdflib import Graph, URIRef, Node
from typing import Optional, Set


def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    """
    Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader
    """
    if roots is None:
        roots = set()

    # Iterate over all nodes in the graph
    for node in graph.nodes():
        # Check if the node has no incoming edges along the prop property
        if not any((node, prop, parent) in graph for parent in graph.predecessors(node)):
            roots.add(node)

    return roots

# Example usage:
# Assuming 'g' is an rdflib.Graph instance with triples of the form (child, rdflib.RDFS.subClassOf, parent)
# g = Graph()
# g.add((child_node, rdflib.RDFS.subClassOf, parent_node))
# ...
# roots = find_roots(g, rdflib.RDFS.subClassOf)
# print(roots)
