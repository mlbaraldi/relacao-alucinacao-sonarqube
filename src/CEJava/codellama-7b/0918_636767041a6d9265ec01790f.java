package generated;
public class Generateddf581e8da222 {
public static Integer[] toObject(final int[] array){
    if (array == null) {
        return null;
    }
    Integer[] objectArray = new Integer[array.length];
    for (int i = 0; i < array.length; i++) {
        objectArray[i] = new Integer(array[i]);
    }
    return objectArray;
}
}
