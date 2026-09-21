

def _eval_file(prefix, file_path):
    file_name, file_extension = file_path.split('.')

    if file_extension == 'asset':
        file_type = 'asset'
    elif file_extension == 'rendition':
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    return {
        'prefix': prefix,
        'file_type': file_type,
        'file_path': file_path
    }
