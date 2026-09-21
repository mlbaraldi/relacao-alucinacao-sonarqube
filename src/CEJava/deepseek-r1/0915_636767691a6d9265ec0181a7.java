package generated;
public class Generated03989cad0315 {
public static String trimLeadingCharacter(String str,char leadingCharacter){
    if (str == null || str.isEmpty()) {
        return str;
    }
    int index = 0;
    while (index < str.length() && str.charAt(index) == leadingCharacter) {
        index++;
    }
    return str.substring(index);
}
}
