package generated;
public class Generated4277de58188d {
public static String[] split(String toSplit,String delimiter){
    int index = toSplit.indexOf(delimiter);
    if (index == -1) {
        return null;
    }
    String before = toSplit.substring(0, index);
    String after = toSplit.substring(index + delimiter.length());
    return new String[] { before, after };
}
}
