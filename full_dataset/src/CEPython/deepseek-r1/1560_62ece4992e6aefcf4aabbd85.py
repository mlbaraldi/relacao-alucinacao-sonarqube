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
    subjects = set()
    objects = set()
    for s, o in graph.subject_objects(prop):
        subjects.add(s)
        objects.add(o)
    computed_roots = objects - subjects
    return computed_roots
