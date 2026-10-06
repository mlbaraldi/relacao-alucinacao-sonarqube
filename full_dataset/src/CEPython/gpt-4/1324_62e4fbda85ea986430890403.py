import random
from typing import Sequence


def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle
    """
    # Create a copy of the sequence so we don't modify the original
    seq_copy = list(seq)
    
    # Use a constant seed for the random number generator
    random.seed(1)
    
    # Shuffle the sequence
    random.shuffle(seq_copy)
    
    return seq_copy
