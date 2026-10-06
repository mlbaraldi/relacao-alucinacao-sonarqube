package generated;
public class Generated963b5016e7d2 {
private JsonObject convertProperties(List<KeyStringValuePair> properties){
    JsonObject jsonObject = new JsonObject();
    for (KeyStringValuePair property : properties) {
        jsonObject.addProperty(property.getKey(), property.getValue());
    }
    return jsonObject;
}
}
