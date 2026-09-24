package generated;
public class Generatedf5705ba67411 {
@SuppressWarnings("unchecked") public String toString(JSONWriter.Feature... features){
    StringWriter sw = new StringWriter();
    JSONWriter writer = new JSONWriter(sw);
    for (JSONWriter.Feature feature : features) {
        writer.config(feature, true);
    }
    writer.write(this);
    writer.flush();
    return sw.toString();
}
}
