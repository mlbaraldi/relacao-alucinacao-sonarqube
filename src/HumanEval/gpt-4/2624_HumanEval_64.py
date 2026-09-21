
FIX =
    s = s.lower()
    count = 0
    for char in s:
        if char in 'aeiou':
            count += 1
    if s.endswith('y'):
        count += 1
    return count
