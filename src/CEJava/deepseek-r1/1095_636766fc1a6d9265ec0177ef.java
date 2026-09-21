package generated;
public class Generated5b7588b58913 {
static String[] toNoNullStringArray(Object[] array){
    if (array == null) {
        return new String[0];
    }

    // Check if the array is already a String array with no nulls
    if (array instanceof String[]) {
        boolean hasNull = false;
        for (String s : (String[]) array) {
            if (s == null) {
                hasNull = true;
                break;
            }
        }
        if (!hasNull) {
            return (String[]) array;
        }
    }

    // Collect non-null elements
    List<String> list = new ArrayList<>();
    for (Object obj : array) {
        if (obj != null) {
            list.add((String) obj);
        }
    }
    return list.toArray(new String[0]);
}
}
