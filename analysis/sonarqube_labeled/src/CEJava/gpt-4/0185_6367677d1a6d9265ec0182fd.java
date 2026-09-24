package generated;
public class Generatedfb4097a6069e {
public static boolean toBoolean(String value,boolean dEfault){
    if (value == null) {
        return dEfault;
    }
    String lowerCaseValue = value.toLowerCase();
    if (lowerCaseValue.equals("true") || lowerCaseValue.equals("false")) {
        return true;
    } else {
        return dEfault;
    }
}
}
