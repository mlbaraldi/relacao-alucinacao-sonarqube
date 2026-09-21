package generated;
public class Generatedd68a7871a262 {
@Override public Action inspect(AtmosphereResource r){
    if (r.getTransport() == AtmosphereResource.TRANSPORT.WEBSOCKET) {
        // Suspend the resource if it's a WebSocket connection
        r.suspend();
        return Action.CONTINUE;
    } else {
        // Continue processing the resource if it's not a WebSocket connection
        return Action.CONTINUE;
    }
}
}
