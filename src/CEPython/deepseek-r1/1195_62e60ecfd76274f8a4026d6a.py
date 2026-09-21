def protocol_handlers(cls, protocol_version=None):
    if protocol_version is not None:
        if not isinstance(protocol_version, tuple):
            raise TypeError("protocol version is not passed in a tuple")
        handlers = cls._protocol_handlers
        if protocol_version in handlers:
            return {protocol_version: handlers[protocol_version]}
        else:
            return {}
    else:
        return dict(cls._protocol_handlers)
