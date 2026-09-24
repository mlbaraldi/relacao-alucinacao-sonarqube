package generated;
public class Generated015c1b574417 {
private static char decodeHexNibble(final char c){
    if(c >= '0' && c <= '9')
        return (char)(c - '0');
    if(c >= 'a' && c <= 'f')
        return (char)(c - 'a' + 10);
    if(c >= 'A' && c <= 'F')
        return (char)(c - 'A' + 10);
    return Character.MAX_VALUE;
}
}
