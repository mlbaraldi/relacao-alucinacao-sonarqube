package generated;
public class Generatedd68a7871a262 {
@Override public Action inspect(AtmosphereResource r){
    if (r.getTransport().equals(AtmosphereResource.Transport.NONE)) {
        r.suspend();
    }
    return Action.CONTINUE;
}
}
