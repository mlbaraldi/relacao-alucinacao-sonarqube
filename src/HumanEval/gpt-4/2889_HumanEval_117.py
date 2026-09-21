
def select_words(s, n):
    if not s:
        return []
    words = s.split()
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return [word for word in words if sum(1 for char in word if char in consonants) == n]
