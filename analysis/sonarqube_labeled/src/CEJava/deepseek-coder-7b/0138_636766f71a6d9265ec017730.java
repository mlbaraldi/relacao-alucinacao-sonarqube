package generated;
public class Generatedc597b5e3aeb0 {
static String[] toNoNullStringArray(Collection<?> collection){
    ArrayList<String> list = new ArrayList<>();
    for (Object obj : collection) {
        if (obj != null) {
            list.add((String) obj);
        }
    }
    return list.toArray(new String[0]);
}
}
