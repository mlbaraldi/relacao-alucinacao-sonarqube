
def exchange(lst1, lst2):
    # Check if both lists are non-empty
    if not lst1 or not lst2:
        return "NO"

    # Check if all elements in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if there is an element in lst2 that is even
    for num in lst2:
        if num % 2 == 0:
            # If there is an even element in lst2, return "YES"
            return "YES"

    # If no even element is found in lst2, return "NO"
    return "NO"
