package generated;
public class Generatedf73469d36770 {
public String id(String entityId){
    // Assuming the entityId is in the format "row_id:entity_id"
    String[] parts = entityId.split(":");
    // Return the row id
    return parts[0];
}
}
