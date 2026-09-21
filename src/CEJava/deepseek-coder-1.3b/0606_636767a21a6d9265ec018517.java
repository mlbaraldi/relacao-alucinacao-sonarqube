package generated;
public class Generatedc486c51583fa {
public final byte[] toByteArray(){
    ByteBuffer buffer = ByteBuffer.allocate(1024); // Allocate a buffer of size 1024
    byte[] bytes = new byte[buffer.position()]; // Create a byte array to hold the buffer contents
    buffer.rewind(); // Rewind the buffer to the start
    buffer.get(bytes); // Get the buffer contents into the byte array
    return bytes; // Return the byte array
}
}
