package generated;
public class Generatedd68a7871a262 {
@Override public Action inspect(AtmosphereResource r){
    if (r.transport().equals(AtmosphereResource.TRANSPORT.LONG_POLLING)) {
        r.suspend();
    } else if (r.transport().equals(AtmosphereResource.TRANSPORT.WEBSOCKET)) {
        r.suspend(-1);
    } else if (r.transport().equals(AtmosphereResource.TRANSPORT.SSE)) {
        r.suspend();
    } else if (r.transport().equals(AtmosphereResource.TRANSPORT.JSONP)) {
        r.suspend();
    } else if (r.transport().equals(AtmosphereResource.TRANSPORT.AJAX)) {
        r.suspend();
    } else if (r.transport().equals(AtmosphereResource.TRANSPORT.STREAMING)) {
        r.suspend();
    }
    return Action.CONTINUE;
}
}
