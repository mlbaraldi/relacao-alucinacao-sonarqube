package generated;
public class Generatedbc5e1082b4e5 {
public static int nextPrime(int desiredCapacity){
    if (desiredCapacity < 2) {
        return 2;
    }

    int next = desiredCapacity;
    boolean found = false;

    while (!found) {
        next++;

        if (isPrime(next)) {
            found = true;
        }
    }

    return next;
}
}
