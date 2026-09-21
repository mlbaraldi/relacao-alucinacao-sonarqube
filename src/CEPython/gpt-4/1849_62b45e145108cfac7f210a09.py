

def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Assuming manifest_files is a dictionary where key is the file name and value is the digest
    # and digests_used is a list of digests that are used

    for file, digest in manifest_files.items():
        if digest not in digests_used:
            print(f"Digest {digest} for file {file} is not used.")
            return False

    # Check if all used digests are present in the manifest
    for used_digest in digests_used:
        if used_digest not in manifest_files.values():
            print(f"Used digest {used_digest} is not present in the manifest.")
            return False

    return True
