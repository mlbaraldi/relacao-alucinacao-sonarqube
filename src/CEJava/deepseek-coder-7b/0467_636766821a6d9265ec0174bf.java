package generated;
public class Generatedc17c420d6329 {
public static String capitalize(String name){
    if (name == null || name.length() == 0) {
        return name;
    }
    return name.toLowerCase().substring(0, 1).toUpperCase() + name.substring(1);
}
}
