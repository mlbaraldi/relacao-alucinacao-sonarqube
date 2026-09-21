package generated;
public class Generated0cd6c9efe8f9 {
public static String[] trimArrayElements(String[] array){
    if (array == null) {
        return null;
    }
    String[] result = new String[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = array[i].trim();
    }
    return result;
}
}
