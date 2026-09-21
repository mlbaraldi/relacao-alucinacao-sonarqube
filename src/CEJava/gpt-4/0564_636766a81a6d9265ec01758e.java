package generated;
public class Generatedbc5e1082b4e5 {
public static int nextPrime(int desiredCapacity){
    if (desiredCapacity <= 1) {
        return 2;
    }
    int prime = desiredCapacity;
    while (true) {
        if (isPrime(prime)) {
            if (desiredCapacity >= 1000) {
                if (prime <= desiredCapacity * 1.11) {
                    return prime;
                }
            } else {
                return prime;
            }
        }
        prime++;
    }
}
}
