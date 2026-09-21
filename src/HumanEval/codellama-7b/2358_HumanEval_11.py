from typing import List


def string_xor(a: str, b: str) -> str:
    result = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            result += "0"
        else:
            result += "1"
    return result
