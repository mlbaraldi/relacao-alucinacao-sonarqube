
def cycpattern_check(a , b):
    # Check if word2 is a substring of word1
    if word2 in word1:
        return True
    
    # Check if any rotations of word2 are substrings of word1
    for i in range(len(word2)):
        rotation = word2[i:] + word2[:i]
        if rotation in word1:
            return True
    
    return False
