package generated;
public class Generated8b0123611be9 {
public void putAllWriteable(BeanMap map){
    for (String propertyName : map.getPropertyNames()) {
        if (map.isWritable(propertyName)) {
            put(propertyName, map.get(propertyName));
        }
    }
}
}
