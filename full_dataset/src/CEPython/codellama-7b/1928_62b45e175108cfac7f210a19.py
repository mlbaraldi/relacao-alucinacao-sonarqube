

def validate_fixity(self, fixity, manifest_files):
    # Check if the fixity block is present
    if not fixity:
        raise ValueError("Fixity block is not present in the inventory")

    # Check if the fixity block is valid
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block is not a dictionary")

    # Check if the fixity block contains the required keys
    required_keys = ["files", "checksums"]
    for key in required_keys:
        if key not in fixity:
            raise ValueError(f"Fixity block is missing required key: {key}")

    # Check if the files listed in the fixity block are present in the manifest
    for file in fixity["files"]:
        if file not in manifest_files:
            raise ValueError(f"File {file} is not present in the manifest")

    # Check if the checksums listed in the fixity block are valid
    for checksum in fixity["checksums"]:
        if not isinstance(checksum, str):
            raise ValueError(f"Checksum {checksum} is not a string")

    # Check if the checksums listed in the fixity block match the files they are associated with
    for file, checksum in fixity["files"].items():
        if checksum != manifest_files[file]["checksum"]:
            raise ValueError(f"Checksum {checksum} does not match the checksum in the manifest for file {file}")

    # If all checks pass, return True
    return True
