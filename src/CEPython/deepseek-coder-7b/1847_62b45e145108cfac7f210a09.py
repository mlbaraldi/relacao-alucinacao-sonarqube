

def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            digests_in_manifest = file.read().splitlines()

        for digest in digests_in_manifest:
            if digest not in digests_used:
                return False

    return True
