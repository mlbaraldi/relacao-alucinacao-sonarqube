

def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    for key in fixity.keys():
        if key not in manifest_files:
            return False
    return True
