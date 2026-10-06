package generated;
public class Generated963b5016e7d2 {
private JsonObject convertProperties(List<KeyStringValuePair> properties){
    JsonObject jsonObject = new JsonObject();
    for (KeyStringValuePair property : properties) {
        jsonObject.add(property.getKey(), new JsonPrimitive(property.getValue()));
    }
    return jsonObject;
}
}
