def get_nested_custom_and_control_args(self, args):
    control_args = {}
    nested_args = {}
    current_key = None
    expecting_value = False
    control_prefix = 'control.'

    for arg in args:
        if expecting_value:
            # This is the value for the current_key
            if current_key.startswith(control_prefix):
                key = current_key[len(control_prefix):]
                control_args[key] = arg
            else:
                nested_args[current_key] = arg
            current_key = None
            expecting_value = False
        elif arg.startswith('--'):
            # New key encountered
            current_key = arg[2:]
            if '=' in current_key:
                # Key-value pair in the same argument
                key_part, value = current_key.split('=', 1)
                if key_part.startswith(control_prefix):
                    control_key = key_part[len(control_prefix):]
                    control_args[control_key] = value
                else:
                    nested_args[key_part] = value
                current_key = None
            else:
                # Key without value, expect the next argument to be the value
                expecting_value = True
        else:
            # This is a value not preceded by a '--' key, assume it's the value for current_key if set
            if current_key is not None:
                if current_key.startswith(control_prefix):
                    key = current_key[len(control_prefix):]
                    control_args[key] = arg
                else:
                    nested_args[current_key] = arg
                current_key = None
                expecting_value = False

    # Handle any dangling current_key without a value (treat as a flag)
    if current_key is not None:
        if current_key.startswith(control_prefix):
            key = current_key[len(control_prefix):]
            control_args[key] = True  # Treat as a boolean flag
        else:
            nested_args[current_key] = True

    return control_args, nested_args
