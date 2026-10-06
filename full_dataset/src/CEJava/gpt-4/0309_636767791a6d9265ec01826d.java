package generated;
public class Generatedff05360ad3f6 {
public static String findAndSubst(String key,Properties props){
    String value = props.getProperty(key);
    if (value == null) {
        return null;
    }

    for (String propKey : props.stringPropertyNames()) {
        String propValue = props.getProperty(propKey);
        value = value.replace("${" + propKey + "}", propValue);
    }

    return value;
}
}
