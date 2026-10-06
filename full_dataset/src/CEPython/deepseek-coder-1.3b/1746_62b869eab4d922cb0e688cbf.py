

def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    `spec.manifest` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """

    # Get all resources in the manifest
    resources = app.spec.manifest.get('resources', [])

    # For each resource, generate a default observer schema
    for resource in resources:
        # Check if a custom observer schema has been specified for this resource
        if 'observerSchema' in resource:
            del resource['observerSchema']

        # If no custom schema has been specified, generate a default one
        else:
            resource['observerSchema'] = {
                'type': 'object',
                'properties': {
                    'key': {
                        'type': 'string'
                    }
                }
            }

    # Update the manifest with the new observer schema
    app.spec.manifest = {
        'resources': resources
    }
