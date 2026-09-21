import os
import json


def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    # Read the plugin's properties from a JSON file
    with open(os.path.join(plugin_dir, 'plugin.json'), 'r') as f:
        plugin_spec = json.load(f)

    # Flatten the dictionary
    flatten_dict = {}
    for key, value in plugin_spec.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flatten_dict[f'{key}.{sub_key}'] = sub_value
        else:
            flatten_dict[key] = value

    return flatten_dict
