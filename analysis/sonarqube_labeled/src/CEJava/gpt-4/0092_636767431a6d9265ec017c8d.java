package generated;
public class Generated14da2c9cee94 {
private int computeBinaryLog(int n){
    if(n <= 0) throw new IllegalArgumentException("Input must be greater than 0");
    return (int)(Math.log(n) / Math.log(2)) + 1;
}
}
