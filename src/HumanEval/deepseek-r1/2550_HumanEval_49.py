

def modp(n: int, p: int):
    result = 1
    base = 2 % p  # Ensure base is within mod p from the start
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2
    return result % p
