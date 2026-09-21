package generated;
public class Generated2a1f5e2d423b {
private Map<String,Object> buildContent(JsonObject jsonObject){
    Map<String, Object> contentMap = new HashMap<>();
    boolean hasAts = jsonObject.has("ats");

    Map<String, Object> atsMap = new HashMap<>();

    for (Map.Entry<String, JsonElement> entry : jsonObject.entrySet()) {
        String key = entry.getKey();
        JsonElement valueElement = entry.getValue();
        Object value = convertJsonElement(valueElement);

        if (!hasAts && key.startsWith("@")) {
            String atKey = key.substring(1);
            atsMap.put(atKey, value);
        } else {
            contentMap.put(key, value);
        }
    }

    if (!hasAts && !atsMap.isEmpty()) {
        contentMap.put("ats", atsMap);
    }

    return contentMap;
}
}
