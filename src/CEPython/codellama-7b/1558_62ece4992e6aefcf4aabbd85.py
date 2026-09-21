import rdflib
from rdflib import Graph, URIRef


def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    if roots is None:
        roots = set()
    for s, p, o in graph:
        if p == prop and o not in roots:
            roots.add(o)
            find_roots(graph, prop, roots)
    return roots
