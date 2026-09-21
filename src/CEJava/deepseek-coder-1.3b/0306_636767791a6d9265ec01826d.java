package generated;
public class Generatedff05360ad3f6 {
public static String findAndSubst(String key,Properties props){
    String value = props.getProperty(key);
    if (value != null) {
        // Perform variable substitution here. For example, you can replace ${variable} with the value of the variable.
        // This is just a simple example, you may need to adjust it according to your needs.
        value = value.replace("${", "").replace("}", "");
    }
    return value;
}
}
