package generated;
public class Generatedaa1c1f0def9f {
public static String[] concatenateStringArrays(String[] array1,String[] array2){
    if (array1 == null && array2 == null) {
        return null;
    }

    if (array1 == null) {
        return array2;
    }

    if (array2 == null) {
        return array1;
    }

    String[] result = new String[array1.length + array2.length];
    System.arraycopy(array1, 0, result, 0, array1.length);
    System.arraycopy(array2, 0, result, array1.length, array2.length);

    return result;
}
}
