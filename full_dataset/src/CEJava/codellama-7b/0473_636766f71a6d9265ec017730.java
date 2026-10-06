package generated;
public class Generatedc597b5e3aeb0 {
static String[] toNoNullStringArray(Collection<?> collection){
    if (collection == null) {
        return null;
    }
    String[] array = new String[collection.size()];
    int i = 0;
    for (Object obj : collection) {
        if (obj != null) {
            array[i++] = obj.toString();
        }
    }
    return array;
}
}
