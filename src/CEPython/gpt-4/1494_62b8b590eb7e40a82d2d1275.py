

def _legacy_mergeOrderings(orderings):
    merged = []
    while orderings:
        for i, ordering in enumerate(orderings):
            if all(ordering[0] not in o or o.index(ordering[0]) == 0 for o in orderings):
                merged.append(ordering.pop(0))
                if not ordering:
                    orderings.pop(i)
                break
        else:
            raise ValueError("Orderings cannot be merged")
    return merged
