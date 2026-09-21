package generated;
public class Generatedbc5e1082b4e5 {
public static int nextPrime(int desiredCapacity){
    if (desiredCapacity <= 2) {
        return 2;
    }
    // Start with the next odd number if desiredCapacity is even
    int candidate = (desiredCapacity % 2 == 0) ? desiredCapacity + 1 : desiredCapacity;
    while (true) {
        if (isPrime(candidate)) {
            return candidate;
        }
        candidate += 2; // Check only odd numbers
    }
}
}
