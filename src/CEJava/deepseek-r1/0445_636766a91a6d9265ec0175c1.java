package generated;
public class Generatedfd078237af10 {
private void enlarge(final int size){
    int currentCapacity = (buffer != null) ? buffer.length : 0;
    if (currentCapacity - count >= size) {
        return;
    }
    int needed = count + size;
    int newCapacity = Math.max(needed, currentCapacity * 2);
    byte[] newBuffer = new byte[newCapacity];
    if (buffer != null) {
        System.arraycopy(buffer, 0, newBuffer, 0, count);
    }
    buffer = newBuffer;
}
}
