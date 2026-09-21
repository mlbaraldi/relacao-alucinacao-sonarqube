def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}
    # Get the state of the given version from the inventory
    version_state = inventory.get(version, {}).get('state', {})
    # Iterate over each logical path in the version's state
    for logical_path, content_file in version_state.items():
        # Extract the checksum of the current content file
        current_checksum = content_file.get('checksum')
        # Collect all content files across all versions with the same checksum
        duplicates = set()
        for ver in inventory.values():
            for cf in ver.get('state', {}).values():
                if cf.get('checksum') == current_checksum:
                    duplicates.add(cf['file_path'])
        logical_path_map[logical_path] = duplicates
    return logical_path_map
