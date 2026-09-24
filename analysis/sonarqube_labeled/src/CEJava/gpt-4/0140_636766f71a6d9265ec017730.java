package generated;
public class Generatedc597b5e3aeb0 {
static String[] toNoNullStringArray(Collection<?> collection){
    if (collection == null) {
        return new String[0];
    }
    List<String> list = new ArrayList<>();
    for (Object obj : collection) {
        if (obj != null) {
            list.add(obj.toString());
        }
    }
    return list.toArray(new String[0]);
}
}
