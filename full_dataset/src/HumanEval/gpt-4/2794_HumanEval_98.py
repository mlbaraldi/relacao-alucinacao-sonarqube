
def count_upper(s):
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):  # iterate over even indices
        if s[i] in vowels:  # check if character is an uppercase vowel
            count += 1
    return count
