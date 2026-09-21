package generated;
public class Generated503fda58ebbd {
private static int digitValue(final char c){
    if (c >= '0' && c <= '9') {
        return c - '0';
    } else if (c >= 'a' && c <= 'z') {
        return 10 + (c - 'a');
    } else if (c >= 'A' && c <= 'Z') {
        return 10 + (c - 'A');
    } else {
        return -1;
    }
}
}
