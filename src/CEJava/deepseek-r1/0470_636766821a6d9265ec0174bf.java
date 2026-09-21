package generated;
public class Generatedc17c420d6329 {
public static String capitalize(String name){
    if (name == null || name.length() == 0) {
        return name;
    }
    char first = name.charAt(0);
    if (Character.isLowerCase(first)) {
        if (name.length() > 1 && Character.isUpperCase(name.charAt(1))) {
            return name;
        } else {
            return Character.toUpperCase(first) + name.substring(1);
        }
    } else {
        return name;
    }
}
}
