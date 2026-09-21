package generated;
public class Generated5becb6ba365a {
public int nonZeros(int row){
    int count = 0;
    while (row != 0) {
        if ((row & 1) != 0) {
            count++;
        }
        row >>>= 1;
    }
    return count;
}
}
