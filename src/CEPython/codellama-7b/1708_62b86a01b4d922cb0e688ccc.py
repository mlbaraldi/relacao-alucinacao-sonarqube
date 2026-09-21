

def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    observer_schema = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value, first_level=first_level)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value, first_level=first_level)
        else:
            observer_schema[key] = None
    if first_level:
        for identifying_field in ['name', 'namespace', 'kind']:
            observer_schema[identifying_field] = manifest_dict[identifying_field]
    return observer_schema
