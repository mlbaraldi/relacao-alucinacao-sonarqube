package generated;
public class Generated0aa471b272fd {
public int compare(Object aObj1,Object aObj2){
    if (aObj1 == null && aObj2 == null) {
        return 0;
    }
    if (aObj1 == null) {
        return -1;
    }
    if (aObj2 == null) {
        return 1;
    }
    if (aObj1.getId() == aObj2.getId()) {
        return 0;
    }
    return aObj1.getId() < aObj2.getId() ? -1 : 1;
}
}
