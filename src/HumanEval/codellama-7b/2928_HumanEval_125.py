
def split_words(txt):
    # Check if the text contains any whitespace
    if ' ' in txt:
        # Split the text on whitespace
        return txt.split()
    # Check if the text contains any commas
    elif ',' in txt:
        # Split the text on commas
        return txt.split(',')
    # If neither whitespace nor commas are present, return the number of lower-case letters with odd order in the alphabet
    else:
        count = 0
        for c in txt:
            if c.islower() and ord(c) % 2 == 1:
                count += 1
        return count
