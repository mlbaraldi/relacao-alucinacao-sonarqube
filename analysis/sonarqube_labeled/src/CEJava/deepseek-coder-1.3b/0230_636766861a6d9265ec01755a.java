package generated;
public class Generatedc68a68cba21a {
public final MatchResult match(CharSequence uri){
    if (uri == null) {
        return MatchResult.NO_MATCH;
    }

    String uriString = uri.toString();
    String[] parts = uriString.split("://");

    if (parts.length != 2) {
        return MatchResult.NO_MATCH;
    }

    String scheme = parts[0];
    String rest = parts[1];

    parts = rest.split("/", 2);

    if (parts.length != 2) {
        return MatchResult.NO_MATCH;
    }

    String host = parts[0];
    String path = parts[1];

    // Assuming path is in the format "scheme://host/path"
    return new MatchResult(scheme, host, path);
}
}
