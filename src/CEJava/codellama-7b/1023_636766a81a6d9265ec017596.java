package generated;
public class Generated7746ec4e0a66 {
public ByteVector putInt(final int intValue){
    // Check if the byte vector needs to be enlarged
    if (size() < 4) {
        // Enlarge the byte vector by 4 bytes
        resize(size() + 4);
    }

    // Write the int value to the byte vector
    for (int i = 0; i < 4; i++) {
        byte b = (byte) (intValue >> (i * 8));
        put(i, b);
    }

    return this;
}
}
