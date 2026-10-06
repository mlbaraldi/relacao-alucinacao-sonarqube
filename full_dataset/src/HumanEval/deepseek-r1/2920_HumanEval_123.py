
def get_odd_collatz(n):
    sequence = [n]
    current = n
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        sequence.append(current)
    odds = [x for x in sequence if x % 2 != 0]
    odds.sort()
    return odds
