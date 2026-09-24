def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in
    ``spec.manifest`` for which a custom observer schema hasn't been specified.

    Args:
        app (krake.data.kubernetes.Application): The application for which to generate a
            default observer schema
    """
    from krake.data.kubernetes import ObserverSchema

    if app.spec.observers is None:
        app.spec.observers = []

    for resource in app.spec.manifest:
        api_version = resource.apiVersion
        kind = resource.kind
        name = resource.metadata.name
        namespace = getattr(resource.metadata, 'namespace', None)

        existing = False
        for observer in app.spec.observers:
            if (observer.api_version == api_version and
                observer.kind == kind and
                observer.name == name and
                getattr(observer, 'namespace', None) == namespace):
                existing = True
                break

        if not existing:
            new_observer = ObserverSchema(
                type="kube",
                api_version=api_version,
                kind=kind,
                name=name,
                namespace=namespace
            )
            app.spec.observers.append(new_observer)
