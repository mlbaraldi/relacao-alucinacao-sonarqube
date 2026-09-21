from rdflib import Graph, URIRef
from typing import Set, Optional


def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    """
    Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    rdflib.RDFS.subClassOf or rdflib.RDF.type
    """
    if roots is None:
        roots = set(graph.subjects(predicate=prop))
    else:
        roots = {node for node in roots if prop in graph.objects(node)}
    return roots
