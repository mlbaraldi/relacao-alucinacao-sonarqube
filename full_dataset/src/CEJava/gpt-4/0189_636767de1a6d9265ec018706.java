package generated;
public class Generated4989c2270303 {
public Mappings diffStructure(String tableName,Mappings mappings){
    Mappings diffMappings = new Mappings();
    Mappings historyMapping = historyMappings.get(tableName);

    if (historyMapping != null) {
        for (Map.Entry<String, String> entry : mappings.getFields().entrySet()) {
            if (!historyMapping.getFields().containsKey(entry.getKey())) {
                diffMappings.addField(entry.getKey(), entry.getValue());
            }
        }
    } else {
        diffMappings = mappings;
    }

    return diffMappings;
}
}
