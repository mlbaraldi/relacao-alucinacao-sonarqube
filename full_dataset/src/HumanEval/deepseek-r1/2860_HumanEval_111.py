
def histogram(test):
    letters = test.split()
    counts = {}
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1
    if not counts:
        return {}
    max_count = max(counts.values())
    return {k: v for k, v in counts.items() if v == max_count}
