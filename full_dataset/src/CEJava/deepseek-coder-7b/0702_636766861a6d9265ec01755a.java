package generated;
public class Generatedc68a68cba21a {
public final MatchResult match(CharSequence uri){
    Matcher matcher = pattern.matcher(uri);
    if (matcher.find()) {
        return new MatchResult(true, matcher.group());
    } else {
        return new MatchResult(false, null);
    }
}
}
