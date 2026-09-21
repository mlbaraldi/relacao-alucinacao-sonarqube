
def is_bored(S):
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    boredoms = 0
    for sentence in sentences:
        if sentence.strip().startswith('I'):
            boredoms += 1
    return boredoms
