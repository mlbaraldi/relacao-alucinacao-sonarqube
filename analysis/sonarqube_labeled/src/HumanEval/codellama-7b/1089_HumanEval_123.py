
def get_odd_collatz(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    sequence = [n]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)

    return sorted(sequence[1:], reverse=True)
