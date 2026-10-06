package generated;
public class Generated4d8d0a34e309 {
public static List<PathSegmentImpl> decodePath(URI u,boolean decode){
    List<PathSegmentImpl> pathSegments = new ArrayList<>();

    if (u.getPath() != null) {
        String[] pathComponents = u.getPath().split("/");
        for (String pathComponent : pathComponents) {
            if (decode) {
                pathComponent = URLDecoder.decode(pathComponent, "UTF-8");
            }
            pathSegments.add(new PathSegmentImpl(pathComponent));
        }
    }

    return pathSegments;
}
}
