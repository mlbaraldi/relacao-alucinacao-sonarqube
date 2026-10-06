package generated;
public class Generatedc68a68cba21a {
public final MatchResult match(CharSequence uri){
    Matcher matcher = pattern.matcher(uri);
    if (!matcher.matches()) {
        return null;
    }
    Map<String, String> variables = new HashMap<>();
    for (int i = 0; i < variableNames.size(); i++) {
        String varName = variableNames.get(i);
        variables.put(varName, matcher.group(i + 1)); // Groups are 1-based
    }
    return new MatchResult(variables);
}
}
