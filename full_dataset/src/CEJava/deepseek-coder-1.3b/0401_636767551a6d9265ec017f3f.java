package generated;
public class Generatedc75982bdb3cf {
public static final <V>void swap(V[] arr,int i,int j){
    // Create a temporary variable to hold the value of the element at index j
    V temp = arr[j];

    // Set the value of the element at index j to the value of the element at index i
    arr[j] = arr[i];

    // Set the value of the element at index i to the value held in the temporary variable
    arr[i] = temp;
}
}
