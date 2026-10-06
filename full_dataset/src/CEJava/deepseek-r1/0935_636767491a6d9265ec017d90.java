package generated;
public class Generated409fa3816830 {
public static final <V>void reverse(V[] arr,int from,int to){
    int start = from;
    int end = to;
    while (start < end) {
        V temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
}
