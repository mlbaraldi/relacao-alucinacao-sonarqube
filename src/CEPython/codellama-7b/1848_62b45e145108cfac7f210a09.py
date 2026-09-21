

def check_digests_present_and_used(self, manifest_files, digests_used):
    # Iterate over the manifest files
    for manifest_file in manifest_files:
        # Read the manifest file
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)

        # Iterate over the digests in the manifest
        for digest in manifest['digests']:
            # Check if the digest is in the list of digests used
            if digest not in digests_used:
                # If the digest is not used, raise an error
                raise ValueError(f"Digest {digest} is not used in the manifest")

            # Check if the digest is present in the manifest
            if digest not in manifest['digests']:
                # If the digest is not present, raise an error
                raise ValueError(f"Digest {digest} is not present in the manifest")

    # If all digests are present and used, return True
    return True
