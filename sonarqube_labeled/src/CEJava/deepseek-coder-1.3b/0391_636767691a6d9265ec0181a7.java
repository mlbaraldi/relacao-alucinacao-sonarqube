package generated;
public class Generated03989cad0315 {
public static String trimLeadingCharacter(String str,char leadingCharacter){
    if (str.length() == 0) {
        return str;
    }

    if (str.charAt(0) == leadingCharacter) {
        return str.substring(1);
    } else {
        return str;
    }
}
}
