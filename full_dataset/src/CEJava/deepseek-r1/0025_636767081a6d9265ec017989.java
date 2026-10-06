package generated;
public class Generated3a055c3787e5 {
public static boolean[] toPrimitive(final Boolean[] array){
    if (array == null) {
        return null;
    }
    final int length = array.length;
    final boolean[] result = new boolean[length];
    for (int i = 0; i < length; i++) {
        Boolean b = array[i];
        if (b == null) {
            throw new NullPointerException("Element at index " + i + " is null");
        }
        result[i] = b.booleanValue();
    }
    return result;
}
}
