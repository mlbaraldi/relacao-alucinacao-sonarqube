package generated;
public class Generated5becb6ba365a {
public int nonZeros(int row){
    int count = 0;
    for(int i = 0; i < row.length; i++){
        if(row[i] != 0){
            count++;
        }
    }
    return count;
}
}
