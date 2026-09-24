
def fix_spaces(text):
    # Replace all spaces in the text with underscores
    text = text.replace(" ", "_")
    
    # If a string has more than 2 consecutive spaces, 
    # then replace all consecutive spaces with -
    while "__" in text:
        text = text.replace("__", "-")
    
    return text
