package generated;
public class Generateddf581e8da222 {
public static Integer[] toObject(final int[] array){
    // Check if the array is null
    if(array == null) {
        return null;
    }

    // Create a new Integer array with the same length as the input array
    Integer[] result = new Integer[array.length];

    // Convert each int in the input array to an Integer and store in the result array
    for(int i = 0; i < array.length; i++) {
        result[i] = array[i];
    }

    // Return the result array
    return result;
}
}
