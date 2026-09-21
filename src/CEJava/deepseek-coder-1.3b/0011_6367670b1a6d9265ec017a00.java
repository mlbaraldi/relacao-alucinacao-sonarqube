package generated;
public class Generatedbbb50bb38e04 {
public static boolean isSameLength(final byte[] array1,final byte[] array2){
    if (array1 == null && array2 == null) {
        return true;
    } else if (array1 == null || array2 == null) {
        return false;
    } else {
        return array1.length == array2.length;
    }
}
}
