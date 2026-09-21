package generated;
public class Generatedfd078237af10 {
private void enlarge(final int size){
    // Check if the byteVector needs to be enlarged
    if (byteVector.length < size) {
        // Create a new byte array with the desired size
        byte[] newByteVector = new byte[size];

        // Copy the existing bytes into the new array
        System.arraycopy(byteVector, 0, newByteVector, 0, byteVector.length);

        // Replace the old byte vector with the new one
        byteVector = newByteVector;
    }
}
}
