

def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    for file in manifest_files:
        if 'digest' not in file:
            raise ValueError(f"Missing 'digest' key in file {file}")
        if file['digest'] not in digests_used:
            raise ValueError(f"Digest {file['digest']} not used in manifest")
    return True
