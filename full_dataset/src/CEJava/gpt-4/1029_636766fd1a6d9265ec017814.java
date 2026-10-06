package generated;
public class Generated33f665e2921b {
public static boolean arrayequals(byte[] a,byte[] b,int count){
    if (a == null || b == null) {
        throw new IllegalArgumentException("Input arrays cannot be null");
    }
    if (count < 0 || count > a.length || count > b.length) {
        throw new IllegalArgumentException("Count is out of range");
    }
    for (int i = 0; i < count; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}
}
