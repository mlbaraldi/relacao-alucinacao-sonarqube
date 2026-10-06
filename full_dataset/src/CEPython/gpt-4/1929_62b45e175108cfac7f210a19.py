

def validate_fixity(self, fixity, manifest_files):
    # Check if fixity is a dictionary
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block should be a dictionary")

    # Check if all files in fixity are in manifest_files
    for file in fixity:
        if file not in manifest_files:
            raise ValueError(f"File {file} in fixity block is not listed in the manifest")

    # If no errors were raised, the fixity block is valid
    return True
