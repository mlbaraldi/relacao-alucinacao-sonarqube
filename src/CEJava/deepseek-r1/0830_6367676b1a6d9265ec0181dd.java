package generated;
public class Generatedd6bc0ba0b76f {
public static int countOccurrencesOf(String str,String sub){
    if (str == null || sub == null || sub.isEmpty()) {
        return 0;
    }
    int count = 0;
    int fromIndex = 0;
    while (true) {
        int index = str.indexOf(sub, fromIndex);
        if (index == -1) {
            break;
        }
        count++;
        fromIndex = index + 1;
    }
    return count;
}
}
