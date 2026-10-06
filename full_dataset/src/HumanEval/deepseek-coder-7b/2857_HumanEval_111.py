
def histogram(test):
    if not test:
        return {}

    words = test.split()
    counts = {}
    max_count = 0
    result = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        if counts[word] > max_count:
            max_count = counts[word]
            result = {word: max_count}
        elif counts[word] == max_count:
            result[word] = max_count

    return result
