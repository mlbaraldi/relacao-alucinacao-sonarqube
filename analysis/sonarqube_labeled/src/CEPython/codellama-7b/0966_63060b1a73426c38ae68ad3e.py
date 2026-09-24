import os
import json


def get_plugin_spec_flatten_dict(plugin_dir):
    # Load the plugin's spec file
    spec_file = os.path.join(plugin_dir, 'plugin.spec')
    with open(spec_file, 'r') as f:
        spec = json.load(f)

    # Flatten the spec dictionary
    flattened_spec = {}
    for key, value in spec.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flattened_spec[f'{key}.{subkey}'] = subvalue
        else:
            flattened_spec[key] = value

    return flattened_spec
