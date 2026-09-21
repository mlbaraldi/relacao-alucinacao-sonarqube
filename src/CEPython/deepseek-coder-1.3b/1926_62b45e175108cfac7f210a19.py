

def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    # Check if fixity is a dictionary
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block should be a dictionary.")

    # Check if all keys in fixity are in manifest_files
    for file_name in fixity.keys():
        if file_name not in manifest_files:
            raise ValueError(f"File {file_name} referenced in fixity block is not in the manifest.")

    # Check if all values in fixity are valid fixity levels
    for file_name, fixity_level in fixity.items():
        if fixity_level not in ['strong', 'weak', 'none']:
            raise ValueError(f"Invalid fixity level for file {file_name}. Valid levels are 'strong', 'weak', 'none'.")

    # If all checks pass, return True
    return True
