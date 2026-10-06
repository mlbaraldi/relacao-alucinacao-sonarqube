package generated;
public class Generatedf5705ba67411 {
@SuppressWarnings("unchecked") public String toString(JSONWriter.Feature... features){
    StringBuilder sb = new StringBuilder();
    sb.append('{');
    boolean first = true;
    for (JSONWriter.Feature feature : features) {
        if (!first) {
            sb.append(", ");
        }
        sb.append(feature.name());
        first = false;
    }
    sb.append('}');
    return sb.toString();
}
}
