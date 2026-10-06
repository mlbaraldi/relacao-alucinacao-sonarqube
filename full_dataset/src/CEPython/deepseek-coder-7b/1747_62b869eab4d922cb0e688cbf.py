from kubernetes import client, config


def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    `spec.manifest` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    api_instance = client.CoreV1Api()

    # Assuming app.spec.manifest contains the list of Kubernetes resources
    for manifest in app.spec.manifest:
        # Check if a custom observer schema is specified for this resource
        if 'observer_schema' not in manifest:
            # Generate a default observer schema
            default_observer_schema = {
                "resource_name": manifest['metadata']['name'],
                "namespace": manifest['metadata']['namespace'],
                "kind": manifest['kind'],
                # Add more default fields as needed
            }

            # Here you would typically save the default observer schema or use it as needed
            print(f"Generated default observer schema for {manifest['metadata']['name']}:")
            print(default_observer_schema)

# Example usage:
# Assuming `app` is an instance of `krake.data.kubernetes.Application` with a `spec.manifest` attribute
# generate_default_observer_schema(app)
