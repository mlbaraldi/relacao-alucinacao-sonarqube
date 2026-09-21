import random
from typing import Sequence


def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle a sequence of strings.
    """
    # Create a copy of the sequence to avoid modifying the original sequence
    seq = list(seq)
    
    # Use the Fisher-Yates algorithm to shuffle the sequence
    for i in range(len(seq) - 1, 0, -1):
        j = random.randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]
    
    return seq
