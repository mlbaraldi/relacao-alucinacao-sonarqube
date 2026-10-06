package generated;
public class Generated4277de58188d {
public static String[] split(String toSplit,String delimiter){
    int index = toSplit.indexOf(delimiter);
    if (index == -1) {
        return null;
    }
    String[] result = new String[2];
    result[0] = toSplit.substring(0, index);
    result[1] = toSplit.substring(index + delimiter.length());
    return result;
}
}
