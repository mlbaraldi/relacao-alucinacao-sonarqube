package generated;
public class Generated3a055c3787e5 {
public static boolean[] toPrimitive(final Boolean[] array){
    if (array == null) {
        return null;
    }

    boolean[] primitiveArray = new boolean[array.length];

    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array content is null at index " + i);
        }
        primitiveArray[i] = array[i];
    }

    return primitiveArray;
}
}
