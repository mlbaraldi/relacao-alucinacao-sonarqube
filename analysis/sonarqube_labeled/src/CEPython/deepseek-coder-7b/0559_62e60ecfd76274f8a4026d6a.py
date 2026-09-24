

def protocol_handlers(cls, protocol_version=None):
    if protocol_version is None:
        return cls.handlers
    elif isinstance(protocol_version, tuple):
        if protocol_version in cls.handlers:
            return {protocol_version: cls.handlers[protocol_version]}
        else:
            raise ValueError(f"Unsupported protocol version: {protocol_version}")
    else:
        raise TypeError("Protocol version must be a tuple")
