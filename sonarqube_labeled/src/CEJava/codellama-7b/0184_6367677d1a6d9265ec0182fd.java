package generated;
public class Generatedfb4097a6069e {
public static boolean toBoolean(String value,boolean dEfault){
    if (value == null) {
        return defaultValue;
    }
    value = value.toLowerCase();
    if (value.equals("true")) {
        return true;
    } else if (value.equals("false")) {
        return false;
    } else {
        return defaultValue;
    }
}
}
