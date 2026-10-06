package generated;
public class Generated7703e1189122 {
public static int[] toPrimitive(final Integer[] array){
    if (array == null) {
        return null;
    }

    int[] primitiveArray = new int[array.length];

    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array content is null");
        }
        primitiveArray[i] = array[i];
    }

    return primitiveArray;
}
}
