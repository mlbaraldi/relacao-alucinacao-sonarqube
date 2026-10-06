package generated;
public class Generated4989c2270303 {
public Mappings diffStructure(String tableName,Mappings mappings){
    Set<String> currentFields = currentMappings.getFieldNames();
    Set<String> historyFields = historyMappings.getFieldNames();

    Map<String, Object> diffFields = new HashMap<>();

    for (String field : currentFields) {
        if (!historyFields.contains(field)) {
            diffFields.put(field, currentMappings.getFields().get(field));
        }
    }

    return new Mappings(diffFields);
}
}
