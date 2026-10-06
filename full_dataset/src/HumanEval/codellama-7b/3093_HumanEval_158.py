
def find_max(words):
    unique_chars = {}
    max_unique_chars = 0
    max_word = ""

    for word in words:
        unique_chars[word] = len(set(word))
        if unique_chars[word] > max_unique_chars:
            max_unique_chars = unique_chars[word]
            max_word = word

    return max_word
