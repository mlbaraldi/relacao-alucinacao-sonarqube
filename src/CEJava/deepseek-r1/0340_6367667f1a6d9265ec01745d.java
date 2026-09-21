package generated;
public class Generated4d8d0a34e309 {
public static List<PathSegmentImpl> decodePath(URI u,boolean decode){
    String rawPath = u.getRawPath();
    if (rawPath == null) {
        rawPath = "";
    }

    boolean isAbsolute = rawPath.startsWith("/");

    List<String> segmentStrings = new ArrayList<>();
    if (isAbsolute) {
        String[] parts = rawPath.split("/", -1);
        for (int i = 1; i < parts.length; i++) {
            segmentStrings.add(parts[i]);
        }
    } else {
        String[] parts = rawPath.split("/", -1);
        Collections.addAll(segmentStrings, parts);
    }

    List<PathSegmentImpl> segments = new ArrayList<>();
    for (String segment : segmentStrings) {
        String[] components = segment.split(";", -1);
        String pathComponent = components.length > 0 ? components[0] : "";
        if (decode) {
            pathComponent = decodeComponent(pathComponent);
        }

        Map<String, String> parameters = new HashMap<>();
        for (int i = 1; i < components.length; i++) {
            String param = components[i];
            if (param.isEmpty()) {
                continue;
            }

            int eqIndex = param.indexOf('=');
            String key = eqIndex == -1 ? param : param.substring(0, eqIndex);
            String value = eqIndex == -1 ? null : param.substring(eqIndex + 1);

            if (decode) {
                key = decodeComponent(key);
                if (value != null) {
                    value = decodeComponent(value);
                }
            }

            parameters.put(key, value);
        }

        segments.add(new PathSegmentImpl(pathComponent, parameters));
    }

    return segments;
}
}
