

def get_spec_defaults(self):
    resolved_args = {}
    for arg_name, default_value in self.spec.items():
        resolved_args[arg_name] = self.get_value_from_source(arg_name) or default_value
    return resolved_args
