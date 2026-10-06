package generated;
public class Generatedf5705ba67411 {
@SuppressWarnings("unchecked") public String toString(JSONWriter.Feature... features){
    ObjectMapper mapper = new ObjectMapper();
    for (JSONWriter.Feature feature : features) {
        mapper.configure(SerializationFeature.valueOf(feature.name()), true);
    }
    try {
        return mapper.writeValueAsString(objectToSerialize);
    } catch (Exception e) {
        throw new RuntimeException("Failed to serialize object to JSON", e);
    }
}
}
