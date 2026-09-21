package generated;
public class Generated03989cad0315 {
public static String trimLeadingCharacter(String str,char leadingCharacter){
    int strLen;
    if (str == null || (strLen = str.length()) == 0) {
        return str;
    }
    int start;
    for (start = 0; start < strLen; start++) {
        if (str.charAt(start) != leadingCharacter) {
            break;
        }
    }
    return str.substring(start);
}
}
