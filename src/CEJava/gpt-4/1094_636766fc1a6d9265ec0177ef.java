package generated;
public class Generated5b7588b58913 {
static String[] toNoNullStringArray(Object[] array){
    if (array == null) {
        return null;
    }
    List<String> list = new ArrayList<>();
    for (Object obj : array) {
        if (obj != null) {
            list.add(obj.toString());
        }
    }
    return list.toArray(new String[0]);
}
}
