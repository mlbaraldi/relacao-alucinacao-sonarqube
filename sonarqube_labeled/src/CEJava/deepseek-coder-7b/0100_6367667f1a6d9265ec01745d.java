package generated;
public class Generated4d8d0a34e309 {
public static List<PathSegmentImpl> decodePath(URI u,boolean decode){
    String path = u.getPath();
    if (path == null) {
        return null;
    }

    // Split the path into segments
    String[] segments = path.split("/");

    // If decode is true, decode each segment
    if (decode) {
        for (int i = 0; i < segments.length; i++) {
            segments[i] = java.net.URLDecoder.decode(segments[i], "UTF-8");
        }
    }

    // Convert the segments into PathSegmentImpl objects and return them
    return Arrays.stream(segments)
            .filter(s -> !s.isEmpty()) // Filter out empty segments
            .map(PathSegmentImpl::new)
            .collect(Collectors.toList());
}
}
