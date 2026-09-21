

def _get_conditionally_required_args(self, command_name, options_spec,
                                         args):
    conditionally_required_args = []
    for option in options_spec:
        if 'required_when' in option:
            required_when = option['required_when']
            for condition in required_when:
                if condition in args and args[condition] == required_when[condition]:
                    conditionally_required_args.append(option['name'])
    return conditionally_required_args
