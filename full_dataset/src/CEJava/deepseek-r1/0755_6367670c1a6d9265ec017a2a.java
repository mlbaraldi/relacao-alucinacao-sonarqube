package generated;
public class Generated7703e1189122 {
public static int[] toPrimitive(final Integer[] array){
    if (array == null) {
        return null;
    }
    int[] result = new int[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = array[i]; // Auto-unboxing here may throw NullPointerException
    }
    return result;
}
}
