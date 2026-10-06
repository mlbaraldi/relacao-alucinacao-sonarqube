def _shuffled(seq: Sequence[str]) -> list[str]:
    import hashlib
    import random
    from typing import Sequence
    hasher = hashlib.sha256()
    for s in seq:
        hasher.update(s.encode('utf-8'))
    hash_digest = hasher.digest()
    rng = random.Random(hash_digest)
    shuffled_list = list(seq)
    rng.shuffle(shuffled_list)
    return shuffled_list
