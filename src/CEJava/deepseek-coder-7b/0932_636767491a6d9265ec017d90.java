package generated;
public class Generated409fa3816830 {
public static final <V>void reverse(V[] arr,int from,int to){
    V temp;
    while (from < to) {
        temp = arr[from];
        arr[from] = arr[to];
        arr[to] = temp;
        from++;
        to--;
    }
}
}
