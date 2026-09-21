

def _eval_file(prefix, file_path):
    # Identify the type of file based on the prefix
    if prefix == "asset":
        file_type = "asset"
    elif prefix == "rendition":
        file_type = "rendition"
    else:
        raise ValueError(f"Invalid prefix: {prefix}")

    # Update the packages dictionary with the file type and path
    packages[file_type] = file_path

    return packages
