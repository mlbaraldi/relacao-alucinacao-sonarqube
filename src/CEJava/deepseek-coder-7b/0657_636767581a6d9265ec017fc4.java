package generated;
public class Generated41c6ea0646ba {
public static long factorial(int n){
    if(n < 0){
        throw new IllegalArgumentException("Input should be non-negative");
    }
    if(n == 0 || n == 1){
        return 1;
    }
    long fact = 1;
    for(int i = 2; i <= n; i++){
        fact *= i;
    }
    return fact;
}
}
