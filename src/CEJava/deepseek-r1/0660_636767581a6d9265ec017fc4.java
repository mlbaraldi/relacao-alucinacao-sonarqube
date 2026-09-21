package generated;
public class Generated41c6ea0646ba {
public static long factorial(int n){
    if (n < 0) {
        throw new IllegalArgumentException("n must be non-negative");
    }
    long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
}
