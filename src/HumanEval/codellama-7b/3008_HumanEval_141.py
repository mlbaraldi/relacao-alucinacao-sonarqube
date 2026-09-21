
def file_name_check(file_name):
    if len(file_name) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if file_name.startswith('.'):
        return 'No'
    if file_name.endswith('.'):
        return 'No'
    if file_name.find('.') == -1:
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
