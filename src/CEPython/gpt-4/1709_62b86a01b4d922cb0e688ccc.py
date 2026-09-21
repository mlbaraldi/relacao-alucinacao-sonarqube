

def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    observer_schema = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value)
        else:
            observer_schema[key] = None if not first_level else value
    return observer_schema
