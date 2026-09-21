
def select_words(s, n):
    if not s:
        return []

    words = s.split()
    result = []

    for word in words:
        count = sum(1 for c in word if c.lower() in 'bcdfghjklmnpqrstvwxyz')
        if count == n:
            result.append(word)

    return result
