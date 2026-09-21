package generated;
public class Generated5b7588b58913 {
static String[] toNoNullStringArray(Object[] array){
    if (array == null) {
        return null;
    }
    List<String> list = new ArrayList<>();
    for (Object element : array) {
        if (element != null) {
            list.add(element.toString());
        }
    }
    return list.toArray(new String[list.size()]);
}
}
