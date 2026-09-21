
FIX =
    count = 0
    if not s:
        return count
    # Process all characters except the last
    for char in s[:-1].lower():
        if char in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    # Process the last character
    last_char = s[-1].lower()
    if last_char in {'a', 'e', 'i', 'o', 'u', 'y'}:
        count += 1
    return count
