
def fix_spaces(text):
    result = ""
    space_count = 0
    for char in text:
        if char == " ":
            space_count += 1
            if space_count > 2:
                result += "-"
            else:
                result += "_"
        else:
            if space_count > 0:
                space_count = 0
                result += "_"
            result += char
    return result

