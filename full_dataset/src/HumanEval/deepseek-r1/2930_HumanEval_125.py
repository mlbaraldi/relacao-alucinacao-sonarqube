
def split_words(txt):
    # Check if any whitespace character exists
    if any(c.isspace() for c in txt):
        return txt.split()
    # Check if commas exist
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count lowercase letters with odd positions
        count = 0
        for c in txt:
            if c.islower():
                pos = ord(c) - ord('a')
                if pos % 2 == 1:
                    count += 1
        return count
