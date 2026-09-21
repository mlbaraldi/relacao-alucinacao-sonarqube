package generated;
public class Generatedff05360ad3f6 {
public static String findAndSubst(String key,Properties props){
    String value = props.getProperty(key);
    if (value == null) {
        throw new IllegalArgumentException("Key not found in properties: " + key);
    }

    Pattern pattern = Pattern.compile("\\$\\{([^}]+)\\}");
}
