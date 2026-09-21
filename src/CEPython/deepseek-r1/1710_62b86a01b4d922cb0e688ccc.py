def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    observer_schema = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value)
        else:
            observer_schema[key] = None
    if first_level:
        # Handle top-level identifying fields: apiVersion and kind
        for field in ['apiVersion', 'kind']:
            if field in manifest_dict:
                observer_schema[field] = manifest_dict[field]
        # Handle metadata.name and metadata.namespace if present
        if 'metadata' in manifest_dict and isinstance(manifest_dict['metadata'], dict):
            original_metadata = manifest_dict['metadata']
            observer_metadata = observer_schema.get('metadata', {})
            # Ensure we only override name and namespace if they exist in the original
            for field in ['name', 'namespace']:
                if field in original_metadata:
                    observer_metadata[field] = original_metadata[field]
            observer_schema['metadata'] = observer_metadata
    return observer_schema
