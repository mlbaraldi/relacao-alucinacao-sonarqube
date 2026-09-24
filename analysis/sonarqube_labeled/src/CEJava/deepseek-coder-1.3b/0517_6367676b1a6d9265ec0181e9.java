package generated;
public class Generated63bc335b5e92 {
public static boolean substringMatch(CharSequence str,int index,CharSequence substring){
    if (str instanceof StringBuilder) {
        StringBuilder sb = (StringBuilder) str;
        return sb.substring(index).equals(substring);
    } else {
        return str.toString().substring(index).equals(substring.toString());
    }
}
}
