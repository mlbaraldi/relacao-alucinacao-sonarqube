
def select_words(s, n):
    words = s.split()
    consonant_words = []
    for word in words:
        if len(word) == n and word.isalpha():
            consonant_words.append(word)
    return consonant_words
