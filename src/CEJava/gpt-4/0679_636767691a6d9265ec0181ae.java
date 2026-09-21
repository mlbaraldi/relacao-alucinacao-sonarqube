package generated;
public class Generated7edd296be0ff {
public static String[] toStringArray(Enumeration<String> enumeration){
    if (enumeration == null) {
        return null;
    }

    List<String> list = Collections.list(enumeration);
    String[] array = new String[list.size()];
    return list.toArray(array);
}
}
