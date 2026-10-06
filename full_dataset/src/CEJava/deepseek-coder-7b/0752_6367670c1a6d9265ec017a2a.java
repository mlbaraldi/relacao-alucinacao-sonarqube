package generated;
public class Generated7703e1189122 {
public static int[] toPrimitive(final Integer[] array){
    // Check if the input array is null
    if (array == null) {
        return null;
    }

    // Create a new int array with the same size as the input array
    int[] result = new int[array.length];

    // Convert each Integer object to an int primitive and store it in the new array
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array content is null");
        }
        result[i] = array[i].intValue();
    }

    // Return the new array
    return result;
}
}
