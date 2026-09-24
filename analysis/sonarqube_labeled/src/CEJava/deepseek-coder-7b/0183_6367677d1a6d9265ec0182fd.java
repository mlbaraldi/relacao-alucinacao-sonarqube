package generated;
public class Generatedfb4097a6069e {
public static boolean toBoolean(String value,boolean dEfault){
    if (value == null) {
        return defaultVal;
    }
    String lowerCaseValue = value.toLowerCase();
    if ("true".equals(lowerCaseValue)) {
        return true;
    } else if ("false".equals(lowerCaseValue)) {
        return false;
    } else {
        return defaultVal;
    }
}
}
