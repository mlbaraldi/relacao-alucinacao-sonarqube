package generated;
public class Generated14da2c9cee94 {
private int computeBinaryLog(int n){
    if (n <= 0) {
        throw new IllegalArgumentException("n must be greater than 0");
    }

    int result = 0;
    while (n > 1) {
        n >>= 1;
        result++;
    }
    return result + 1;
}
}
