

def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    result = ""
    indent_str = " " * indent
    if debug:
        result += f"{indent_str}<type: {type(self)}, id: {id(self)}>\n"
    if isinstance(self, dict):
        for key, value in self.items():
            result += f"{indent_str}{key}: {pretty(value, indent + 2, debug)}\n"
    elif isinstance(self, list):
        for i, value in enumerate(self):
            result += f"{indent_str}[{i}]: {pretty(value, indent + 2, debug)}\n"
    else:
        result += f"{indent_str}{self}\n"
    return result
