

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle a sequence of strings.
    """
    # Create a list of indices that will be used to shuffle the sequence
    indices = list(range(len(seq)))
    
    # Shuffle the indices using a deterministic algorithm
    for i in range(len(seq)):
        j = i + 1
        indices[i], indices[j] = indices[j], indices[i]
    
    # Use the shuffled indices to create a new list of shuffled strings
    shuffled = [seq[i] for i in indices]
    
    return shuffled
