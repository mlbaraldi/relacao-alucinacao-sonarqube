package generated;
public class Generatedd6bc0ba0b76f {
public static int countOccurrencesOf(String str,String sub){
    if (str == null || sub == null) {
        return 0;
    }
    int count = 0;
    int idx = 0;
    while ((idx = str.toLowerCase().indexOf(sub.toLowerCase(), idx)) != -1) {
        count++;
        idx += sub.length();
    }
    return count;
}
}
