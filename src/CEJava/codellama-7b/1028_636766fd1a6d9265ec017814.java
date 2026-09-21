package generated;
public class Generated33f665e2921b {
public static boolean arrayequals(byte[] a,byte[] b,int count){
    if (a == null || b == null) {
        return false;
    }
    if (count > a.length || count > b.length) {
        return false;
    }
    for (int i = 0; i < count; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}
}
