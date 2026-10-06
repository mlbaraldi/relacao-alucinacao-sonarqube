package generated;
public class Generatedeb189c65687e {
public static double[] toPrimitive(final Double[] array){
    if (array == null) {
        return null;
    }
    int length = array.length;
    double[] result = new double[length];
    for (int i = 0; i < length; i++) {
        result[i] = array[i]; // Auto-unboxing throws NullPointerException if array[i] is null
    }
    return result;
}
}
