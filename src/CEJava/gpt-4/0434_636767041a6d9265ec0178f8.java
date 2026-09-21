package generated;
public class Generatede3e7741b7d0f {
private static String[] copyStrings(final String[] src){
    if(src == null) {
        return null;
    }
    
    String[] dst = new String[src.length];
    
    for(int i = 0; i < src.length; i++){
        if(src[i] != null) {
            dst[i] = src[i].toLowerCase();
        } else {
            dst[i] = null;
        }
    }
    
    return dst;
}
}
