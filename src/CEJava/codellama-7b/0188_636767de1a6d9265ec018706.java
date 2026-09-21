package generated;
public class Generated4989c2270303 {
public Mappings diffStructure(String tableName,Mappings mappings){
    // Get the current index mapping
    Mappings currentMappings = getCurrentMappings(tableName);

    // Get the difference between the current index mapping and the input mapping
    Mappings diff = currentMappings.diff(mappings);

    // Filter out the _source field from the difference
    diff.remove("_source");

    return diff;
}
}
