

def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    if isinstance(parser_dict, dict):
        for key, value in parser_dict.items():
            if isinstance(value, str) and value.startswith('include dict'):
                include_dict_name = value.split(' ')[-1]
                # Here you would need to implement the logic to find and return the included dict
                # For now, I'll just return a placeholder
                return self.find_included_dict(include_dict_name)
            elif isinstance(value, dict):
                # Recursively call this function if the value is a dict
                parser_dict[key] = self._include_groups(value)
        return parser_dict
    else:
        return parser_dict
