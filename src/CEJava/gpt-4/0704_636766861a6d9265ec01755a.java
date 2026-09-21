package generated;
public class Generatedc68a68cba21a {
public final MatchResult match(CharSequence uri){
    Matcher matcher = pattern.matcher(uri);
    if (matcher.matches()) {
        return matcher.toMatchResult();
    } else {
        return null;
    }
}
}
