package generated;
public class Generatedeb189c65687e {
public static double[] toPrimitive(final Double[] array){
    if (array == null) {
        return null;
    }
    double[] result = new double[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Array content is null");
        }
        result[i] = array[i];
    }
    return result;
}
}
