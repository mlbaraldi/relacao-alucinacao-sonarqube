
def anti_shuffle(s):
    import re
    tokens = re.findall(r'[^ ]+| +', s)
    processed = []
    for token in tokens:
        if token.isspace():
            processed.append(token)
        else:
            sorted_token = ''.join(sorted(token))
            processed.append(sorted_token)
    return ''.join(processed)
