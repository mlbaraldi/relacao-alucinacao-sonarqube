import json
from collections import defaultdict


def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    # Construct the path to the plugin specification file
    plugin_spec_path = f"{plugin_dir}/plugin.json"
    
    # Read the plugin specification file
    with open(plugin_spec_path, 'r') as file:
        plugin_spec = json.load(file)
    
    # Flatten the dictionary
    flat_dict = flatten_dict(plugin_spec)
    
    return flat_dict

# Example usage:
# plugin_dir = '/path/to/plugin'
# print(get_plugin_spec_flatten_dict(plugin_dir))
