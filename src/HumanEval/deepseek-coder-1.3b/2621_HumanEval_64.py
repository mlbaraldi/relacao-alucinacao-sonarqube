
FIX =
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    if s[-1].lower() == "y":
        count += 1
    return count
