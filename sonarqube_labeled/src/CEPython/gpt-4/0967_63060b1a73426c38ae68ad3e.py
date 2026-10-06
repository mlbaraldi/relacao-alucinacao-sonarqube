import os
import json
import collections


def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    plugin_spec_path = os.path.join(plugin_dir, 'plugin_spec.json')
    with open(plugin_spec_path, 'r') as f:
        plugin_spec = json.load(f)
    return flatten(plugin_spec)
