

def get_spec_defaults(self):
    # Initialize an empty dictionary to store the resolved defaults
    resolved_defaults = {}

    # Iterate over the spec's arguments
    for arg in self.spec.args:
        # Check if the argument has a default value
        if arg.default is not None:
            # If the argument has a default value, add it to the resolved defaults dictionary
            resolved_defaults[arg.name] = arg.default
        else:
            # If the argument does not have a default value, check if it has a default value in the other sources
            if arg.name in self.other_sources:
                # If the argument has a default value in the other sources, add it to the resolved defaults dictionary
                resolved_defaults[arg.name] = self.other_sources[arg.name]

    return resolved_defaults
