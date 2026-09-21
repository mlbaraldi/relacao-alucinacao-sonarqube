def pretty(self, indent=0, debug=False):
    indent_str = ' ' * indent
    debug_info = f" [id={id(self)}]" if debug else ""
    class_name = self.__class__.__name__
    parts = [f"{indent_str}{class_name}{debug_info}"]
    for key, value in vars(self).items():
        if key.startswith('_'):
            continue
        if hasattr(value, 'pretty'):
            child_str = value.pretty(indent + 2, debug)
        else:
            child_str = repr(value)
        child_lines = child_str.split('\n')
        child_str = '\n'.join([' ' * (indent + 2) + line for line in child_lines])
        parts.append(f"{indent_str}  {key}: {child_str}")
    return '\n'.join(parts)
