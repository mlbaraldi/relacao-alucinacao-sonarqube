def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    processed = set()
    
    def process_group(group_name):
        if group_name in processed:
            return
        processed.add(group_name)
        group = parser_dict.get(group_name)
        if group is None:
            raise KeyError(f"Group '{group_name}' not found in parser_dict.")
        if 'include' not in group:
            return
        includes = group['include']
        # Process each included group first
        for include_name in includes:
            if include_name not in parser_dict:
                raise ValueError(f"Included group '{include_name}' not found in parser_dict.")
            process_group(include_name)
        # Merge the included groups into the current group
        merged = {}
        for include_name in includes:
            merged.update(parser_dict[include_name])
        # Add current group's own entries, excluding 'include'
        current_entries = {k: v for k, v in group.items() if k != 'include'}
        merged.update(current_entries)
        # Update the group in the parser_dict
        parser_dict[group_name] = merged
    
    # Process all groups in the parser_dict
    for group_name in list(parser_dict.keys()):
        process_group(group_name)
