package generated;
public class Generated963b5016e7d2 {
private JsonObject convertProperties(List<KeyStringValuePair> properties){
    JsonObject jsonObject = new JsonObject();
    for (KeyStringValuePair pair : properties) {
        jsonObject.addProperty(pair.getKey(), pair.getValue());
    }
    return jsonObject;
}
}
