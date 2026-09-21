package generated;
public class Generatedc597b5e3aeb0 {
static String[] toNoNullStringArray(Collection<?> collection){
    List<String> result = new ArrayList<>();
    for (Object obj : collection) {
        String s = String.valueOf(obj);
        if (s != null) {
            result.add(s);
        }
    }
    return result.toArray(new String[0]);
}
}
