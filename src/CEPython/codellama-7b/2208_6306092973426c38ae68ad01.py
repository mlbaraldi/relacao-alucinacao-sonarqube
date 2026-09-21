

def get_deprecated_args(self):
    deprecated_args = {}
    for arg in self.args:
        if arg.deprecated:
            deprecated_args[arg.name] = arg.deprecation_message
    return deprecated_args
