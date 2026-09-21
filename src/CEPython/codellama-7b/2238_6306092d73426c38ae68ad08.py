

def _get_conditionally_required_args(self, command_name, options_spec,
                                         args):
    required_args = []
    for option in options_spec:
        if option.get("required_when"):
            condition = option["required_when"]
            if condition(command_name, args):
                required_args.append(option["name"])
    return required_args
