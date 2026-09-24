def get_plugin_spec_flatten_dict(plugin_dir):
    import os
    import yaml
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    spec_path = os.path.join(plugin_dir, 'plugin_spec.yaml')
    with open(spec_path, 'r') as f:
        spec = yaml.safe_load(f)
    
    def flatten(d, parent_key='', sep='.'):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten(v, new_key, sep))
            else:
                items[new_key] = v
        return items
    
    return flatten(spec)
