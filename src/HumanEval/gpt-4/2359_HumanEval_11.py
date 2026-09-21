from typing import List


def string_xor(a: str, b: str) -> str:
    # Convert the strings to integers, perform XOR, then convert back to binary and strip the '0b' prefix
    result = bin(int(a, 2) ^ int(b, 2))[2:]
    # Pad the result with leading zeros to match the length of the longest input string
    return result.zfill(max(len(a), len(b)))
