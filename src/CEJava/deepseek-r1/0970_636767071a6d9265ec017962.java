package generated;
public class Generated8b0123611be9 {
public void putAllWriteable(BeanMap map){
    for (Object keyObj : map.keySet()) {
        String propertyName = (String) keyObj;
        // Check if the source BeanMap can read the property
        if (map.getReadMethod(propertyName) == null) {
            continue;
        }
        // Check if this BeanMap can write the property
        if (this.getWriteMethod(propertyName) == null) {
            continue;
        }
        // Get the value from the source and put into this BeanMap
        Object value = map.get(propertyName);
        this.put(propertyName, value);
    }
}
}
