

def _legacy_mergeOrderings(orderings):
    merged_ordering = []
    for ordering in orderings:
        for item in ordering:
            if item not in merged_ordering:
                merged_ordering.append(item)
    return merged_ordering
