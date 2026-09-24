package generated;
public class Generatede078462cf99f {
public void abbreviate(final int nameStart,final StringBuffer buf){
    if (nameStart < 0 || nameStart >= buf.length()) {
        throw new IllegalArgumentException("Invalid name start index");
    }

    int end = buf.length();
    while (end > nameStart && Character.isLetter(buf.charAt(end - 1))) {
        end--;
    }

    buf.replace(nameStart, end, buf.substring(nameStart, end));
}
}
