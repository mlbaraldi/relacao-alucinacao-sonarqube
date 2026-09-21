package generated;
public class Generated0aa471b272fd {
public int compare(Object aObj1,Object aObj2){
    if (aObj1.getClass() != aObj2.getClass()) {
        throw new IllegalArgumentException("Both objects must be of the same class");
    }
    return ((Comparable) aObj1).compareTo(aObj2);
}
}
