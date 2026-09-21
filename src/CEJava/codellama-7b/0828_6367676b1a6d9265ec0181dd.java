package generated;
public class Generatedd6bc0ba0b76f {
public static int countOccurrencesOf(String str,String sub){
    if (str == null || sub == null) {
        return 0;
    }

    int count = 0;
    int index = str.indexOf(sub);
    while (index != -1) {
        count++;
        index = str.indexOf(sub, index + sub.length());
    }
    return count;
}
}
