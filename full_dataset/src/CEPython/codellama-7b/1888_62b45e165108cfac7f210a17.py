

def get_logical_path_map(inventory, version):
    logical_path_map = {}
    for file in inventory:
        if file['version'] == version:
            logical_path = file['logical_path']
            if logical_path not in logical_path_map:
                logical_path_map[logical_path] = set()
            logical_path_map[logical_path].add(file['content_file'])
    return logical_path_map
