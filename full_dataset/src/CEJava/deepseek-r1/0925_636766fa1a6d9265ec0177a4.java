package generated;
public class Generated10058f865448 {
public static Double[] toObject(final double[] array){
    if (array == null) {
        return null;
    }
    final int length = array.length;
    if (length == 0) {
        return new Double[0];
    }
    final Double[] result = new Double[length];
    for (int i = 0; i < length; i++) {
        result[i] = array[i];
    }
    return result;
}
}
