package generated;
public class Generated91bfb64e4006 {
final String readUtf(final int constantPoolEntryIndex,final char[] charBuffer){
    // Read the CONSTANT_Utf8 entry from the class file buffer
    int utf8EntryOffset = classFileBuffer.getInt(constantPoolEntryIndex);
    int utf8EntryLength = classFileBuffer.getInt(utf8EntryOffset);

    // Check if the buffer is large enough to hold the string
    if (charBuffer.length < utf8EntryLength) {
        throw new IllegalArgumentException("Buffer is too small to hold the string");
    }

    // Read the string from the class file buffer
    classFileBuffer.get(utf8EntryOffset + 4, charBuffer, 0, utf8EntryLength);

    // Return the string
    return new String(charBuffer, 0, utf8EntryLength);
}
}
