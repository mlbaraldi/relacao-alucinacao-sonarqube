package generated;
public class Generatedbc5e1082b4e5 {
public static int nextPrime(int desiredCapacity){
    // Check if the desired capacity is already prime
    if (isPrime(desiredCapacity)) {
        return desiredCapacity;
    }

    // Find the next prime number that is greater than or equal to the desired capacity
    int prime = desiredCapacity;
    while (!isPrime(prime)) {
        prime++;
    }

    // If the desired capacity is greater than or equal to 1000, check if the prime number is within 11% of the desired capacity
    if (desiredCapacity >= 1000 && Math.abs(desiredCapacity - prime) / desiredCapacity > 0.11) {
        // If the prime number is not within 11% of the desired capacity, find the next prime number that is within 11% of the desired capacity
        while (Math.abs(desiredCapacity - prime) / desiredCapacity > 0.11) {
            prime++;
        }
    }

    return prime;
}
}
