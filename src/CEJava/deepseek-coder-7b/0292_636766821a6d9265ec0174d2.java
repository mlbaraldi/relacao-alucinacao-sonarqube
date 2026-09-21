package generated;
public class Generated1958deeb31ae {
public static AtmosphereRequest wrap(HttpServletRequest request){
    AtmosphereResource resource = new AtmosphereResourceImpl(request, null);
    AtmosphereRequest atmosphereRequest = resource.getRequest();
    return atmosphereRequest;
}
}
