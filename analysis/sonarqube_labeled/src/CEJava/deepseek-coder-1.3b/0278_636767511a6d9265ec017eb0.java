package generated;
public class Generated5becb6ba365a {
public int nonZeros(int row){
    int count = 0;
    // Assuming row is an array of integers
    int[] arr = new int[row.length];
    for(int i = 0; i < row.length; i++){
        arr[i] = row[i];
    }
    for(int i = 0; i < arr.length; i++){
        if(arr[i] != 0){
            count++;
        }
    }
    return count;
}
}
