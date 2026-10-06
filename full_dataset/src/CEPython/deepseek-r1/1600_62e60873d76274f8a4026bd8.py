def protocol_handlers(cls, protocol_version=None):
    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("protocol version must be a tuple")
        available_handlers = cls._protocol_handlers
        if protocol_version in available_handlers:
            return {protocol_version: available_handlers[protocol_version]}
        else:
            return {}
    else:
        return cls._protocol_handlers.copy()
