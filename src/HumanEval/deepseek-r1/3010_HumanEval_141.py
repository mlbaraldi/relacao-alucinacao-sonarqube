
def file_name_check(file_name):
    # Check the number of digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Split the file name into parts based on the dot
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    name_part, ext_part = parts
    
    # Check the name part (before the dot)
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check the extension part (after the dot)
    if ext_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # All conditions are satisfied
    return 'Yes'
