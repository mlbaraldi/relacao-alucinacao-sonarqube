def subclasses(cls):
    """
    Return all subclasses of a class, recursively
    """
    visited = set()
    result = []
    def helper(c):
        for sub in c.__subclasses__():
            if sub not in visited:
                visited.add(sub)
                result.append(sub)
                helper(sub)
    helper(cls)
    return result
