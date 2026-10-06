package generated;
public class Generated9c67fae26902 {
public static Object findFirstMatch(Collection source,Collection candidates){
    for (Object candidate : candidates) {
        if (source.contains(candidate)) {
            return candidate;
        }
    }
    return null;
}
}
