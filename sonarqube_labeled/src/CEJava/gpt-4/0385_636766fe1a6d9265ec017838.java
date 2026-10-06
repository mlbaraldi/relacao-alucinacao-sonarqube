package generated;
public class Generated25bdec35e21f {
public static char[] toPrimitive(final Character[] array){
    if (array == null) {
        return null;
    }
    char[] result = new char[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array element is null at index " + i);
        }
        result[i] = array[i];
    }
    return result;
}
}
