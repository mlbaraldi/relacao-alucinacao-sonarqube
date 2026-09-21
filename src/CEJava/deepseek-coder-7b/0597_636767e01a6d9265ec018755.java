package generated;
public class Generated2a1f5e2d423b {
private Map<String,Object> buildContent(JsonObject jsonObject){
    Map<String, Object> content = new HashMap<>();
    if (jsonObject.has("ats")) {
        content.put("ats", jsonObject.get("ats"));
    }
    // Add other fields from jsonObject to content if needed
    // ...
    return content;
}
}
