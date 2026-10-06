package generated;
public class Generatedd4bf100ad64b {
private String buildContentRange(){
    // Calculate the total number of bytes in the file
    long totalBytes = file.length();

    // Calculate the starting byte of the range
    long startByte = range.getStart();

    // Calculate the ending byte of the range
    long endByte = range.getEnd();

    // Build the 'Content-Range' header value
    return "bytes " + startByte + "-" + endByte + "/" + totalBytes;
}
}
