

def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    # Check if the 'include' directive is in the parser_dict
    if 'include' not in parser_dict:
        return parser_dict

    # Get the list of keys to include
    include_keys = parser_dict['include']

    # Create a new dictionary with only the keys to include
    included_dict = {key: parser_dict[key] for key in include_keys if key in parser_dict}

    return included_dict
