package generated;
public class Generatedeb189c65687e {
public static double[] toPrimitive(final Double[] array){
    if (array == null) {
        return null;
    }

    double[] primitiveArray = new double[array.length];

    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array content is null at index " + i);
        }
        primitiveArray[i] = array[i];
    }

    return primitiveArray;
}
}
