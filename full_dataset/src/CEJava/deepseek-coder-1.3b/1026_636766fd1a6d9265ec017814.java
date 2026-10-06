package generated;
public class Generated33f665e2921b {
public static boolean arrayequals(byte[] a,byte[] b,int count){
    if (a.length != b.length) {
        return false;
    }
    if (count > a.length) {
        count = a.length;
    }
    for (int i = 0; i < count; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}
}
