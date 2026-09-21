package generated;
public class Generatedfb4097a6069e {
public static boolean toBoolean(String value,boolean dEfault){
    if (value == null) {
        return dEfault;
    }
    String lowerValue = value.toLowerCase();
    if ("true".equals(lowerValue) || "false".equals(lowerValue)) {
        return true;
    }
    return dEfault;
}
}
