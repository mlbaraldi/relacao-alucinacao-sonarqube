package generated;
public class Generatedc597b5e3aeb0 {
static String[] toNoNullStringArray(Collection<?> collection){
    List<String> list = new ArrayList<>();
    for (Object o : collection) {
        if (o != null) {
            list.add((String) o);
        }
    }
    return list.toArray(new String[0]);
}
}
