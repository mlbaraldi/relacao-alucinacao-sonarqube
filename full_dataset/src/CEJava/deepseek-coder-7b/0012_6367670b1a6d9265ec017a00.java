package generated;
public class Generatedbbb50bb38e04 {
public static boolean isSameLength(final byte[] array1,final byte[] array2){
    if (array1 == null) {
        return (array2 == null || array2.length == 0);
    } else {
        return (array2 == null || array2.length == 0) ? false : array1.length == array2.length;
    }
}
}
