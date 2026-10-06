package generated;
public class Generatedaa1c1f0def9f {
public static String[] concatenateStringArrays(String[] array1,String[] array2){
    if (array1 == null && array2 == null) {
        return null;
    }

    int totalLength = (array1 != null ? array1.length : 0) + (array2 != null ? array2.length : 0);
    String[] result = new String[totalLength];

    int index = 0;
    if (array1 != null) {
        for (String element : array1) {
            result[index++] = element;
        }
    }
    if (array2 != null) {
        for (String element : array2) {
            result[index++] = element;
        }
    }

    return result;
}
}
