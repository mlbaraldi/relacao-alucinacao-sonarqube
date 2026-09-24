package generated;
public class Generated409fa3816830 {
public static final <V>void reverse(V[] arr,int from,int to){
    if (from < 0 || to >= arr.length || from > to) {
        throw new IllegalArgumentException("Invalid range");
    }

    int left = from;
    int right = to;

    while (left < right) {
        // Swap elements
        V temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        // Move pointers
        left++;
        right--;
    }
}
}
