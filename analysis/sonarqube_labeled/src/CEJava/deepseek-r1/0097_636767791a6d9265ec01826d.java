package generated;
public class Generatedff05360ad3f6 {
public static String findAndSubst(String key,Properties props){
    String value = props.getProperty(key);
    if (value == null) {
        return null;
    }
    
    String previous;
    do {
        previous = value;
        value = substituteVariables(previous, props);
    } while (!value.equals(previous));
    
    return value;
}
}
