
def file_name_check(file_name):
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into name and extension
    name, extension = file_name.split('.')
    
    # Check if the name starts with a latin alphabet letter
    if not name[0].isalpha():
        return 'No'
    
    # Check if the name contains more than three digits
    if sum(c.isdigit() for c in name) > 3:
        return 'No'
    
    # Check if the extension is one of the allowed extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all checks passed, the file name is valid
    return 'Yes'
