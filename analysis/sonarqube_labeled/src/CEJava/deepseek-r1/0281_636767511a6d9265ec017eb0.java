package generated;
public class Generated5becb6ba365a {
public int nonZeros(int row){
    int count = 0;
    for (int value : data[row]) {
        if (value != 0) {
            count++;
        }
    }
    return count;
}
}
