

def match(filename):
    supported_types = ['.txt', '.csv', '.json']
    file_extension = os.path.splitext(filename)[1]
    return file_extension in supported_types
