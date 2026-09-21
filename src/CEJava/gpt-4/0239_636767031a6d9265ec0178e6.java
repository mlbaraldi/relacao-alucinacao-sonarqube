package generated;
public class Generated6a22b3742a3b {
public static byte[] toPrimitive(final Byte[] array){
    if (array == null) {
        return null;
    }
    byte[] result = new byte[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array element is null");
        }
        result[i] = array[i];
    }
    return result;
}
}
