
def is_bored(S):
    import re
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sent in sentences:
        sent_clean = sent.strip()
        if sent_clean:
            words = sent_clean.split()
            if words and words[0] == 'I':
                count += 1
    return count
