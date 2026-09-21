package generated;
public class Generated4277de58188d {
public static String[] split(String toSplit,String delimiter){
    int delimiterIndex = toSplit.indexOf(delimiter);
    
    if (delimiterIndex == -1) {
        return null;
    }
    
    String beforeDelimiter = toSplit.substring(0, delimiterIndex);
    String afterDelimiter = toSplit.substring(delimiterIndex + delimiter.length());
    
    return new String[] {beforeDelimiter, afterDelimiter};
}
}
