package generated;
public class Generated9d029afd55f0 {
private boolean containsAllFields(Fields fields){
    for (String field : fields.properties.stringPropertyNames()) {
        if (!properties.containsKey(field)) {
            return false;
        }
    }
    return true;
}
}
