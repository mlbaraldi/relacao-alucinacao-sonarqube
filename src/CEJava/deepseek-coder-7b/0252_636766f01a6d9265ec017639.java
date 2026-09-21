package generated;
public class Generated0c0638ee0e94 {
public static <T>List<T> asList(T[] a){
    if (a == null) {
        throw new NullPointerException();
    }
    List<T> list = new ArrayList<T>();
    for (T t : a) {
        list.add(t);
    }
    return list;
}
}
