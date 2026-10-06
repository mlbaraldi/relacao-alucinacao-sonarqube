package generated;
public class Generated7b72b9475c1e {
public static char[] clone(final char[] array){
    if (array == null) {
        return null;
    }
    char[] result = new char[array.length];
    System.arraycopy(array, 0, result, 0, array.length);
    return result;
}
}
