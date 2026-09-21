
def generate_integers(a, b):
    start = min(a, b)
    end = max(a, b)
    result = []
    for num in range(start, end + 1):
        if all(int(c) % 2 == 0 for c in str(num)):
            result.append(num)
    return result
