package generated;
public class Generateda9f5130099d4 {
private void enlarge(final int size){
    // First, we need to find out how many bytes are already in the byte vector.
    int currentSize = byteVector.size();

    // If the size is larger than the current size, we need to allocate more memory.
    if(size > currentSize){
        // We create a new byte array with the new size.
        byte[] newByteVector = new byte[size];

        // We copy the old byte vector to the new one.
        System.arraycopy(byteVector, 0, newByteVector, 0, currentSize);

        // We update the reference to the new byte vector.
        byteVector = newByteVector;
    }
}
}
