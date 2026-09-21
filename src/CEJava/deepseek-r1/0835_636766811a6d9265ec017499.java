package generated;
public class Generated241e1c808d94 {
private boolean checkDuplicate(final List<AtmosphereInterceptor> interceptorList,Class<? extends AtmosphereInterceptor> c){
    for (AtmosphereInterceptor interceptor : interceptorList) {
        if (interceptor.getClass() == c) {
            return false;
        }
    }
    return true;
}
}
