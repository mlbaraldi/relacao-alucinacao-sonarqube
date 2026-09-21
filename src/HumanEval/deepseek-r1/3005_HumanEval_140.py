
def fix_spaces(text):
    import re
    return re.sub(r' +', lambda x: '-' if len(x.group()) > 2 else '_' * len(x.group()), text)
