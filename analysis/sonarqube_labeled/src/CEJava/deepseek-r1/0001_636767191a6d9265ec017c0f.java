package generated;
public class Generateda9f5130099d4 {
private void enlarge(final int size){
    int requiredCapacity = count + size;
    if (buffer.length < requiredCapacity) {
        int newCapacity = Math.max(buffer.length * 2, requiredCapacity);
        buffer = Arrays.copyOf(buffer, newCapacity);
    }
}
}
