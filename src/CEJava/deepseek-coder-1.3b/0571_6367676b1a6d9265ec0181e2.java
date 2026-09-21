package generated;
public class Generated9c67fae26902 {
public static Object findFirstMatch(Collection source,Collection candidates){
    Iterator sourceIterator = source.iterator();
    while (sourceIterator.hasNext()) {
        Object sourceElement = sourceIterator.next();
        if (candidates.contains(sourceElement)) {
            return sourceElement;
        }
    }
    return null;
}
}
