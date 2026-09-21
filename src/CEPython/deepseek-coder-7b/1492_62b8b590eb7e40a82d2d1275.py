

def _legacy_mergeOrderings(orderings):
Here is a Python solution for the problem. The idea is to use a set to keep track of the elements that have been processed and a list to keep the result. We iterate over the orderings in the order they are given, and for each ordering, we add the elements that have not been processed yet to the result.

```python
def _mergeOrderings(orderings):
    processed = set()
    result = []
    for ordering in orderings:
        for element in ordering:
            if element not in processed:
                result.append(element)
                processed.add(element)
    return result
