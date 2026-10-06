package generated;
public class Generatedd68a7871a262 {
@Override public Action inspect(AtmosphereResource r){
    if (r.getTransport() != AtmosphereResource.TRANSPORT.WEB_SOCKET) {
        r.suspend();
    }
    return Action.CONTINUE;
}
}
