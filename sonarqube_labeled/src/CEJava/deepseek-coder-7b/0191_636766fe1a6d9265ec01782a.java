package generated;
public class Generated91bfb64e4006 {
final String readUtf(final int constantPoolEntryIndex,final char[] charBuffer){
    // Get the class file buffer
    byte[] classFileBuffer = getClassFileBuffer();

    // Calculate the start and end indices of the CONSTANT_Utf8 entry in the class file buffer
    int startIndex = constantPoolEntryIndex * 4;
    int endIndex = startIndex + 4;

    // Convert the bytes to an integer
    int utf8Index = ((classFileBuffer[startIndex + 3] & 0xFF) << 24) |
                    ((classFileBuffer[startIndex + 2] & 0xFF) << 16) |
                    ((classFileBuffer[startIndex + 1] & 0xFF) << 8) |
                    (classFileBuffer[startIndex] & 0xFF);

    // Calculate the start and end indices of the UTF-8 string in the class file buffer
    startIndex = utf8Index;
    endIndex = startIndex;
    while (endIndex < classFileBuffer.length && classFileBuffer[endIndex] != 0) {
        endIndex++;
    }

    // Convert the bytes to a string
    String utf8String = new String(classFileBuffer, startIndex, endIndex - startIndex, "UTF-8");

    // Copy the string to the char buffer
    System.arraycopy(utf8String.toCharArray(), 0, charBuffer, 0, Math.min(utf8String.length(), charBuffer.length));

    // Return the string
    return utf8String;
}
}
