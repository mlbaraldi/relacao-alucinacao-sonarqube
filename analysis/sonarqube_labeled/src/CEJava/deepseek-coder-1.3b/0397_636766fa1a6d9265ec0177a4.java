package generated;
public class Generated10058f865448 {
public static Double[] toObject(final double[] array){
    // Check if the array is null
    if(array == null) {
        return null;
    }

    // Create a new Double array with the same size as the input array
    Double[] result = new Double[array.length];

    // Convert each element in the input array to a Double and store it in the result array
    for(int i = 0; i < array.length; i++) {
        result[i] = array[i];
    }

    // Return the result array
    return result;
}
}
