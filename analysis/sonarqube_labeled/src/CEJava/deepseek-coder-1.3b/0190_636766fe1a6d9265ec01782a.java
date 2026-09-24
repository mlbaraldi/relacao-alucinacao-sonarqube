package generated;
public class Generated91bfb64e4006 {
final String readUtf(final int constantPoolEntryIndex,final char[] charBuffer){
    // The constant pool table is stored in a byte array.
    // Each entry in the table is an integer representing the index of a UTF-8 string.
    // The first byte of the integer represents the length of the string, in bytes.
    // The remaining bytes represent the UTF-8 characters of the string.
    // The length of the byte array is the total length of the constant pool table.
    // The index of the UTF-8 string in the table is the sum of the length of the constant pool table and the index of the constant pool entry.

    int tableLength = classFileBuffer.length;
    int stringLength = classFileBuffer[constantPoolEntryIndex];
    int index = constantPoolEntryIndex + tableLength;

    // Read the UTF-8 string from the byte array.
    // The string is stored in the byte array starting at the index of the constant pool entry.
    // The length of the string is stored in the first byte of the constant pool entry.
    // The string is stored in the byte array in UTF-8 format.
    // The string is read into the charBuffer.

    System.arraycopy(classFileBuffer, index, charBuffer, 0, stringLength);
    charBuffer[stringLength] = '\u0000'; // Null terminate the string

    return new String(charBuffer, 0, stringLength);
}
}
