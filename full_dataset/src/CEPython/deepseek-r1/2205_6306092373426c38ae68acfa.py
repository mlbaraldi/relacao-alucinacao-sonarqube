def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    resolved = {}
    for param in self.spec:
        name = param['name']
        default = param.get('default')
        resolved[name] = getattr(self, name, default)
    return resolved
