package generated;
public class Generated0c0638ee0e94 {
public static <T>List<T> asList(T[] a){
    return new AbstractList<T>() {
        @Override
        public T get(int index) {
            return a[index];
        }

        @Override
        public int size() {
            return a.length;
        }
    };
}
}
