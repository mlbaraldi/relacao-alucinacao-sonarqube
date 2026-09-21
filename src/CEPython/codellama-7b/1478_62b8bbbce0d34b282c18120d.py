

def is_file_exist(file_name):
    if not file_name:
        return False
    try:
        with open(file_name, 'r'):
            return True
    except FileNotFoundError:
        return False
