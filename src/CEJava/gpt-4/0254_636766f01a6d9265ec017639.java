package generated;
public class Generated0c0638ee0e94 {
public static <T>List<T> asList(T[] a){
    if (a == null) {
        return new ArrayList<>();
    } else {
        List<T> list = new ArrayList<>(a.length);
        for (T item : a) {
            list.add(item);
        }
        return list;
    }
}
}
