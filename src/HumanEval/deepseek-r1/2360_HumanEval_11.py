from typing import List


def string_xor(a: str, b: str) -> str:
    from typing import List
    max_length = max(len(a), len(b))
    a_padded = a.zfill(max_length)
    b_padded = b.zfill(max_length)
    result = []
    for a_char, b_char in zip(a_padded, b_padded):
        if a_char != b_char:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
