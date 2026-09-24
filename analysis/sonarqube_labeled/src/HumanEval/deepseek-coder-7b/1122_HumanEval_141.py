
def file_name_check(file_name):
    pattern = r'^[a-zA-Z]\w*\.\d{0,3}\.(txt|exe|dll)$'
    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'
