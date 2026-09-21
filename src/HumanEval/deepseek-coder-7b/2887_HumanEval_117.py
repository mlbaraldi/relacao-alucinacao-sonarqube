
def select_words(s, n):
    if not s:
        return []

    vowels = set('aeiouAEIOU')
    words = s.split()
    result = []

    for word in words:
        if sum(1 for char in word if char not in vowels) == n:
            result.append(word)

    return result
