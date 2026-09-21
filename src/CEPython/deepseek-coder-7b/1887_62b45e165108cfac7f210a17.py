

def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}

    # Iterate over each item in the inventory
    for item in inventory:
        # Check if the item's version is less than or equal to the specified version
        if item['version'] <= version:
            # If the logical path is already in the map, add the file to its set
            if item['logical_path_in_state'] in logical_path_map:
                logical_path_map[item['logical_path_in_state']].add(item['file_on_disk'])
            else:
                # Otherwise, create a new set with the file and add it to the map
                logical_path_map[item['logical_path_in_state']] = {item['file_on_disk']}

    return logical_path_map

# Example usage:
