def select_filenames_by_prefix(prefix, files):
    import os
    selected_files = []
    for file_path in files:
        filename = os.path.basename(file_path)
        if filename.startswith(prefix):
            selected_files.append(file_path)
    return selected_files
