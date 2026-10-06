
def file_name_check(file_name):
    # Check if the file's name is valid
    if len(file_name) > 3 or file_name[0] == '0' or not file_name.endswith('.') or not file_name[1:].isalpha() or file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'
