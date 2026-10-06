package generated;
public class Generated9d029afd55f0 {
private boolean containsAllFields(Fields fields){
    // Check if fields is null
    if(fields == null){
        return false;
    }

    // Check if each field is null or empty
    if(fields.field1 == null || fields.field2 == null || fields.field3 == null){
        return false;
    }

    // If all fields are not null or empty, return true
    return true;
}
}
