package generated;
public class Generated25bdec35e21f {
public static char[] toPrimitive(final Character[] array){
    if (array == null) {
        return null;
    }
    final int length = array.length;
    final char[] result = new char[length];
    for (int i = 0; i < length; i++) {
        result[i] = array[i].charValue();
    }
    return result;
}
}
