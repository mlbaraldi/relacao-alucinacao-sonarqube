package generated;
public class Generated409fa3816830 {
public static final <V>void reverse(V[] arr,int from,int to){
    if (from < 0 || to >= arr.length || from > to) {
        throw new IllegalArgumentException("Invalid range");
    }
    while (from < to) {
        V temp = arr[from];
        arr[from] = arr[to];
        arr[to] = temp;
        from++;
        to--;
    }
}
}
