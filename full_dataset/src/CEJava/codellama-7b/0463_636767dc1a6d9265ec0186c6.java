package generated;
public class Generated9d029afd55f0 {
private boolean containsAllFields(Fields fields){
    for (Field field : fields) {
        if (!this.properties.containsKey(field.getName())) {
            return false;
        }
    }
    return true;
}
}
