

def _legacy_mergeOrderings(orderings):
Here is a Python solution using list comprehension and the built-in `set` data structure:

```python
def _mergeOrderings(orderings):
    merged = set()
    for ordering in orderings:
        merged.update(ordering)
    return list(merged)
