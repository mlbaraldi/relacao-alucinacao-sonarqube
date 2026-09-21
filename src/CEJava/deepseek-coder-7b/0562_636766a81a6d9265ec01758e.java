package generated;
public class Generatedbc5e1082b4e5 {
public static int nextPrime(int desiredCapacity){
    if (desiredCapacity <= 1) {
        return 2;
    }
    int primeCandidate = desiredCapacity;
    if (primeCandidate % 2 == 0) {
        primeCandidate++;
    }
    while (true) {
        if (isPrime(primeCandidate)) {
            if (primeCandidate >= desiredCapacity && primeCandidate < desiredCapacity * 1.11) {
                return primeCandidate;
            } else if (primeCandidate >= desiredCapacity * 1.11) {
                return (int) Math.ceil(desiredCapacity * 1.11);
            }
        }
        primeCandidate += 2;
    }
}
}
