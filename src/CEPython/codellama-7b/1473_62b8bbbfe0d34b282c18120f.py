

def file_to_textbuffer(file_name, encoding):
    try:
        with open(file_name, 'r', encoding=encoding) as f:
            text = f.read()
        return text
    except FileNotFoundError:
        return None
