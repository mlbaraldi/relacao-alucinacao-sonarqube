

def protocol_handlers(cls, protocol_version=None):
    if protocol_version is None:
        # Return all available versions
        return {(3, 5): ProtocolHandler((3, 5)), (3, 4): ProtocolHandler((3, 4)), (3, 3): ProtocolHandler((3, 3))}
    elif isinstance(protocol_version, tuple):
        # Return a single version
        return {protocol_version: ProtocolHandler(protocol_version)}
    else:
        raise TypeError("Protocol version must be a tuple")
