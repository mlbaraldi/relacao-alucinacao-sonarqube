
def find_max(words):
    if not words:
        return ""
    best_word = words[0]
    max_count = len(set(best_word))
    for word in words[1:]:
        current_count = len(set(word))
        if current_count > max_count:
            max_count = current_count
            best_word = word
        elif current_count == max_count:
            if word < best_word:
                best_word = word
    return best_word
