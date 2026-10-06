import random
from typing import Sequence


def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle a sequence of strings.
    """
    if seed is not None:
        random.seed(seed)
    return random.sample(seq, len(seq))
