
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    words = [word for word in txt.split(' ') if word]
    if not words:
        return False
    last_word = words[-1]
    return len(last_word) == 1 and last_word[0] == last_char
