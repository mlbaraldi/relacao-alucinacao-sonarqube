package generated;
public class Generated4eaba0839589 {
public static byte convertHexDigit(byte b){
    char c = (char) b;
    if (c >= '0' && c <= '9') {
        return (byte) (c - '0');
    } else if (c >= 'A' && c <= 'F') {
        return (byte) (c - 'A' + 10);
    } else if (c >= 'a' && c <= 'f') {
        return (byte) (c - 'a' + 10);
    } else {
        throw new IllegalArgumentException("Invalid hex digit: " + c);
    }
}
}
