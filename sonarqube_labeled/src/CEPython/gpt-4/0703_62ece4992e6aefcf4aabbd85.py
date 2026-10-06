from typing import Optional, Set
from rdflib import Graph, URIRef, Node


def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()

    for s, p, o in graph:
        if p == prop and s not in roots:
            roots.add(s)
            find_roots(graph, prop, roots)

    return roots
