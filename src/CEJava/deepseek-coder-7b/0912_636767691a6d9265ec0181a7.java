package generated;
public class Generated03989cad0315 {
public static String trimLeadingCharacter(String str,char leadingCharacter){
    if (str == null || str.isEmpty()) {
        return str;
    }

    int startIndex = 0;
    while (startIndex < str.length() && str.charAt(startIndex) == leadingCharacter) {
        startIndex++;
    }

    return str.substring(startIndex);
}
}
