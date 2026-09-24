package generated;
public class Generated4277de58188d {
public static String[] split(String toSplit,String delimiter){
    int index = toSplit.indexOf(delimiter);
    if (index == -1) {
        return null;
    }
    String beforeDelimiter = toSplit.substring(0, index);
    String afterDelimiter = toSplit.substring(index + delimiter.length());
    return new String[]{beforeDelimiter, afterDelimiter};
}
}
