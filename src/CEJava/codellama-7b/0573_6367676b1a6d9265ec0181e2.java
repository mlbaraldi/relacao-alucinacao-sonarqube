package generated;
public class Generated9c67fae26902 {
public static Object findFirstMatch(Collection source,Collection candidates){
    for (Object element : source) {
        if (candidates.contains(element)) {
            return element;
        }
    }
    return null;
}
}
