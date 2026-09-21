package generated;
public class Generated409fa3816830 {
public static final <V>void reverse(V[] arr,int from,int to){
    if (from < 0 || from > arr.length || to < 0 || to > arr.length || from > to) {
        throw new IllegalArgumentException("Invalid range");
    }

    for (int i = from, j = to; i < j; i++, j--) {
        V temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
}
