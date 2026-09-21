package generated;
public class Generatedaa1c1f0def9f {
public static String[] concatenateStringArrays(String[] array1,String[] array2){
    if (array1 == null && array2 == null) {
        return null;
    }
    int len1 = (array1 != null) ? array1.length : 0;
    int len2 = (array2 != null) ? array2.length : 0;
    String[] result = new String[len1 + len2];
    if (array1 != null) {
        System.arraycopy(array1, 0, result, 0, len1);
    }
    if (array2 != null) {
        System.arraycopy(array2, 0, result, len1, len2);
    }
    return result;
}
}
