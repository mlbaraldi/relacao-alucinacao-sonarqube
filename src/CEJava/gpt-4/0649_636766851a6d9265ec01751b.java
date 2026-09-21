package generated;
public class Generated015c1b574417 {
private static char decodeHexNibble(final char c){
    if (c >= '0' && c <= '9') {
        return (char) (c - '0');
    } else if (c >= 'a' && c <= 'f') {
        return (char) (c - 'a' + 10);
    } else if (c >= 'A' && c <= 'F') {
        return (char) (c - 'A' + 10);
    } else {
        return Character.MAX_VALUE;
    }
}
}
