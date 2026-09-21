package generated;
public class Generated5b7588b58913 {
static String[] toNoNullStringArray(Object[] array){
    if (array == null) {
        return null;
    }

    String[] noNullArray = new String[array.length];
    int count = 0;

    for (Object obj : array) {
        if (obj instanceof String) {
            noNullArray[count] = (String) obj;
            count++;
        }
    }

    noNullArray = Arrays.copyOf(noNullArray, count);
    return noNullArray;
}
}
