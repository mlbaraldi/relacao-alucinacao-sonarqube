package generated;
public class Generatedc68a68cba21a {
public final MatchResult match(CharSequence uri){
    // Initialize the match result
    MatchResult result = new MatchResult();

    // Get the pattern and the URI
    String pattern = getPattern();
    String uriString = uri.toString();

    // Check if the pattern is a valid regular expression
    if (!Pattern.matches(pattern)) {
        throw new IllegalArgumentException("Invalid pattern: " + pattern);
    }

    // Compile the pattern into a regular expression
    Pattern regex = Pattern.compile(pattern);

    // Match the URI against the regular expression
    Matcher matcher = regex.matcher(uriString);
    if (matcher.matches()) {
        // If the URI matches the pattern, extract the parameters
        result.setParameters(matcher.groupCount());
        for (int i = 1; i <= matcher.groupCount(); i++) {
            result.addParameter(matcher.group(i));
        }
    }

    return result;
}
}
