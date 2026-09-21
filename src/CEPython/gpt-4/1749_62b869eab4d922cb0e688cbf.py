from krake.data.kubernetes import Application


def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    spec.manifest for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    default_observer_schema = {}

    # Assuming that app.spec.manifest is a dictionary where keys are resource names
    # and values are their respective schemas
    for resource, schema in app.spec.manifest.items():
        # If a custom observer schema hasn't been specified, generate a default one
        if 'observer_schema' not in schema:
            default_observer_schema[resource] = 'default_observer_schema'

    return default_observer_schema
