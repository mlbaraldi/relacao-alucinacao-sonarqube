

def triples_sum_to_zero(l: list):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
