
def fix_spaces(text):
    # Replace all consecutive spaces with -
    text = re.sub(' {3,}', '-', text)
    # Replace all remaining spaces with _
    text = text.replace(' ', '_')
    return text
