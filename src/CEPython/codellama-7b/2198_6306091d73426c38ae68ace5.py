

def _include_groups(self, parser_dict):
    # Get the list of groups from the parser_dict
    groups = parser_dict.get('groups', [])

    # Iterate over the groups and include their definitions
    for group in groups:
        # Get the group name and definition from the parser_dict
        group_name = group.get('name')
        group_definition = group.get('definition')

        # Include the group definition in the parser_dict
        parser_dict['groups'][group_name] = group_definition

    # Return the updated parser_dict
    return parser_dict
