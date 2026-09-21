

def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    Together with :func:``generate_default_observer_schema_list``, this function is
    called recursively to generate part of a default ``observer_schema`` from part of
    a Kubernetes resource, defined respectively by ``manifest_dict`` or ``manifest_list``.

    Args:
        manifest_dict (dict): Partial Kubernetes resources
        first_level (bool, optional): If True, indicates that the dictionary represents
            the whole observer schema of a Kubernetes resource

    Returns:
        dict: Generated partial observer_schema

    This function creates a new dictionary from ``manifest_dict`` and replaces all
    non-list and non-dict values by ``None``.

    In case of ``first_level`` dictionary (i.e. complete ``observer_schema`` for a
    resource), the values of the identifying fields are copied from the manifest file.
    """
    if not isinstance(manifest_dict, dict):
        return None

    new_dict = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            new_dict[key] = generate_default_observer_schema_dict(value, first_level=first_level)
        elif isinstance(value, list):
            new_dict[key] = [generate_default_observer_schema_dict(item, first_level=first_level) for item in value]
        else:
            new_dict[key] = value if not first_level else None

    return new_dict
