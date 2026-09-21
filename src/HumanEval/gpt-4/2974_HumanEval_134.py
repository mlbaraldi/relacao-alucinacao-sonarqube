
def check_if_last_char_is_a_letter(txt):
    if not txt:  # if the string is empty
        return False
    if txt[-1] == ' ':  # if the last character is a space
        return False
    if txt[-1].isalpha():  # if the last character is a letter
        if len(txt) == 1 or txt[-2] == ' ':  # if the string has only one character or the second last character is a space
            return True
    return False
