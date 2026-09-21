package generated;
public class Generated9c67fae26902 {
public static Object findFirstMatch(Collection source,Collection candidates){
    if (source == null || candidates == null) {
        return null;
    }
    Set sourceSet = new HashSet(source);
    for (Object candidate : candidates) {
        if (sourceSet.contains(candidate)) {
            return candidate;
        }
    }
    return null;
}
}
