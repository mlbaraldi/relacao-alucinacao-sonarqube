
def fix_spaces(text):
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # If there are more than 2 consecutive spaces, replace them with -
    text = text.replace("__", "-")
    
    return text
