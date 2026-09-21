

def get_logical_path_map(inventory, version):
    logical_path_map = {}
    for state_version, state_files in inventory.items():
        if state_version <= version:
            for logical_path, content_files in state_files.items():
                if logical_path not in logical_path_map:
                    logical_path_map[logical_path] = set()
                logical_path_map[logical_path].update(content_files)
    return logical_path_map
