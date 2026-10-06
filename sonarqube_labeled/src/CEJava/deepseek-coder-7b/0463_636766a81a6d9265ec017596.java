package generated;
public class Generated7746ec4e0a66 {
public ByteVector putInt(final int intValue){
    // Check if the array is large enough
    if (this.size + 4 > this.bytes.length) {
        // Create a new array that is twice as large
        byte[] newBytes = new byte[this.bytes.length * 2];
        // Copy the old array into the new array
        System.arraycopy(this.bytes, 0, newBytes, 0, this.bytes.length);
        // Use the new array
        this.bytes = newBytes;
    }

    // Put the int into the array
    this.bytes[this.size++] = (byte)((intValue >> 24) & 0xFF);
    this.bytes[this.size++] = (byte)((intValue >> 16) & 0xFF);
    this.bytes[this.size++] = (byte)((intValue >> 8) & 0xFF);
    this.bytes[this.size++] = (byte)(intValue & 0xFF);

    return this;
}
}
