package generated;
public class Generated4d8d0a34e309 {
public static List<PathSegmentImpl> decodePath(URI u,boolean decode){
    List<PathSegmentImpl> pathSegments = new ArrayList<>();
    String path = u.getPath();
    if (path.startsWith("/")) {
        path = path.substring(1);
    }
    String[] segments = path.split("/");
    for (String segment : segments) {
        if (decode) {
            segment = URLDecoder.decode(segment, StandardCharsets.UTF_8);
        }
        pathSegments.add(new PathSegmentImpl(segment));
    }
    return pathSegments;
}
}
