package generated;
public class Generatedd68a7871a262 {
@Override public Action inspect(AtmosphereResource r){
    // Get the transport type
    AtmosphereResource.TRANSPORT transport = r.transport();

    // Suspend the resource based on the transport type
    switch (transport) {
        case WEBSOCKET:
        case SSE:
        case LONG_POLLING:
            // Suspend the resource
            r.suspend();
            break;
        default:
            // Do nothing or throw an exception if the transport is not supported
            break;
    }

    // Continue processing
    return Action.CONTINUE;
}
}
