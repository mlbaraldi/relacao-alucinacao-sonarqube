
def get_max_triples(n):
    # Create the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Count the number of elements in a that are 0, 1, or 2 mod 3
    counts = [0, 0, 0]
    for num in a:
        counts[num % 3] += 1
    
    # The number of triples is the sum of the combinations of 3 elements from each group
    return counts[0] * (counts[0] - 1) * (counts[0] - 2) // 6 + \
           counts[1] * (counts[1] - 1) * (counts[1] - 2) // 6 + \
           counts[2] * (counts[2] - 1) * (counts[2] - 2) // 6 + \
           counts[0] * counts[1] * counts[2]
