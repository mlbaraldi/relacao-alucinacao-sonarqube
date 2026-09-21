

def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    observer_schema = {}

    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value, first_level=False)
        elif isinstance(value, list):
            observer_schema[key] = [None if not isinstance(i, (dict, list)) else i for i in value]
        else:
            observer_schema[key] = None if not isinstance(value, (dict, list)) else value

    if first_level:
        for key, value in manifest_dict.items():
            if isinstance(value, dict):
                observer_schema[key] = value

    return observer_schema
