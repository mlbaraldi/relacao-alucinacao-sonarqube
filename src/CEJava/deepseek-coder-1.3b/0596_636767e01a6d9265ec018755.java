package generated;
public class Generated2a1f5e2d423b {
private Map<String,Object> buildContent(JsonObject jsonObject){
    Map<String, Object> content = new HashMap<>();

    // Check if 'ats' is set in the JSON object
    if (jsonObject.has("ats")) {
        // Get the 'ats' value
        Object ats = jsonObject.get("ats");

        // Add the 'ats' value to the content map
        content.put("ats", ats);
    }

    return content;
}
}
