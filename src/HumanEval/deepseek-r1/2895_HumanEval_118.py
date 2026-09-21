
def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    n = len(word)
    if n < 3:
        return ""
    for i in range(n-2, 0, -1):
        current = word[i]
        if current in vowels:
            prev = word[i-1]
            next_char = word[i+1]
            if prev not in vowels and next_char not in vowels:
                return current
    return ""
