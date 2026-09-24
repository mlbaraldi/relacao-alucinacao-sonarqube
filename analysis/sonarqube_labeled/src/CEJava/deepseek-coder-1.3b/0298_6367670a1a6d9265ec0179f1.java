package generated;
public class Generated9460841892ff {
public static Short[] toObject(final short[] array){
    // Check if the array is null
    if(array == null) {
        return null;
    }

    // Create a new Short array with the same length as the input array
    Short[] result = new Short[array.length];

    // Convert each element in the input array to a Short object and store it in the result array
    for(int i = 0; i < array.length; i++) {
        result[i] = Short.valueOf(array[i]);
    }

    // Return the result array
    return result;
}
}
