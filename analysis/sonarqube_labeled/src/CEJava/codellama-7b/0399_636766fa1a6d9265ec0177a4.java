package generated;
public class Generated10058f865448 {
public static Double[] toObject(final double[] array){
    if (array == null) {
        return null;
    }
    Double[] objectArray = new Double[array.length];
    for (int i = 0; i < array.length; i++) {
        objectArray[i] = Double.valueOf(array[i]);
    }
    return objectArray;
}
}
