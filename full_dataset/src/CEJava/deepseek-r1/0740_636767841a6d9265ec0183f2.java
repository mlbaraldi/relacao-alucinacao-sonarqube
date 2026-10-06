package generated;
public class Generated0aa471b272fd {
public int compare(Object aObj1,Object aObj2){
    if (aObj1 == aObj2) {
        return 0;
    }
    if (aObj1 == null) {
        return -1;
    }
    if (aObj2 == null) {
        return 1;
    }
    return ((Comparable)aObj1).compareTo(aObj2);
}
}
