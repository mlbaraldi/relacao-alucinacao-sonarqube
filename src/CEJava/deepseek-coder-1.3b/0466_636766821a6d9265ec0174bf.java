package generated;
public class Generatedc17c420d6329 {
public static String capitalize(String name){
    if (name == null || name.length() == 0) {
        return name;
    }
    return Character.toUpperCase(name.charAt(0)) + name.substring(1);
}
}
