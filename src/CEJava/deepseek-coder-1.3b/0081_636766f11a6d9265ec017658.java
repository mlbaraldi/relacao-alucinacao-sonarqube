package generated;
public class Generatedbbb2f58a37f8 {
public static int indexOfLastSeparator(String filename){
    if (filename == null) {
        return -1;
    }

    int lastSeparatorIndex = -1;
    for (int i = 0; i < filename.length(); i++) {
        char c = filename.charAt(i);
        if (c == '\\' || c == '/') {
            lastSeparatorIndex = i;
        }
    }

    return lastSeparatorIndex;
}
}
