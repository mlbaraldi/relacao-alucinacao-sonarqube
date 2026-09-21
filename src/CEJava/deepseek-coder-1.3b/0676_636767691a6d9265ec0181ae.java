package generated;
public class Generated7edd296be0ff {
public static String[] toStringArray(Enumeration<String> enumeration){
    List<String> list = new ArrayList<String>();
    while(enumeration.hasMoreElements()){
        list.add(enumeration.nextElement());
    }
    return list.toArray(new String[0]);
}
}
