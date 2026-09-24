
FIX =
    count = 0
    for c in s:
        if c in "aeiouy" and c != "y" or c == "y" and s[-1] == "y":
            count += 1
    return count
