package generated;
public class Generatede078462cf99f {
public void abbreviate(final int nameStart,final StringBuffer buf){
    String[] words = nameStart.split(" ");
    for(String word : words){
        buf.append(word.charAt(0));
    }
}
}
