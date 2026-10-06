def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    present_digests = {f.digest for f in manifest_files}
    digests_used_set = set(digests_used)
    
    errors = []
    
    missing = digests_used_set - present_digests
    if missing:
        errors.append(f"Digests used but not present: {missing}")
    
    unused = present_digests - digests_used_set
    if unused:
        errors.append(f"Digests present but not used: {unused}")
    
    if errors:
        raise ValueError("\n".join(errors))
