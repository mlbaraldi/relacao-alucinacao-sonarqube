

def generate_default_observer_schema(app):
    # Get the list of Kubernetes resources present in the application's manifest
    resources = app.spec.manifest.get('resources', [])

    # Create a dictionary to store the default observer schema for each resource
    default_observer_schema = {}

    # Iterate over each resource in the manifest
    for resource in resources:
        # Get the resource type and name
        resource_type = resource['type']
        resource_name = resource['name']

        # Check if a custom observer schema has been specified for this resource
        if resource_type in app.spec.observer_schema:
            # If a custom observer schema has been specified, use it
            default_observer_schema[resource_type] = app.spec.observer_schema[resource_type]
        else:
            # If no custom observer schema has been specified, generate a default one
            default_observer_schema[resource_type] = {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'object',
                        'properties': {
                            'phase': {
                                'type': 'string',
                                'enum': ['Pending', 'Running', 'Succeeded', 'Failed', 'Unknown']
                            }
                        }
                    }
                }
            }

    # Return the default observer schema
    return default_observer_schema
