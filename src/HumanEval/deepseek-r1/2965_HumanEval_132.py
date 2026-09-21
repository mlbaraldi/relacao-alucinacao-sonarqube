
def is_nested(string):
    open_count = string.count('[')
    close_count = string.count(']')
    if open_count < 2 or close_count < 2:
        return False
    
    # Find the index of the second '['
    second_open_pos = -1
    count = 0
    for i, char in enumerate(string):
        if char == '[':
            count += 1
            if count == 2:
                second_open_pos = i
                break
    
    # Check the substring after the second '['
    substring = string[second_open_pos + 1:]
    return substring.count(']') >= 2
