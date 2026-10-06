package generated;
public class Generated6a22b3742a3b {
public static byte[] toPrimitive(final Byte[] array){
    if (array == null) {
        return null;
    }
    final byte[] result = new byte[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = array[i].byteValue();
    }
    return result;
}
}
