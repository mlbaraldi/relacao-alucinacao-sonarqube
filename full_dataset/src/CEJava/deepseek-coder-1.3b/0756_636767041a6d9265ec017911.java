package generated;
public class Generated6b36a08d3a39 {
static void register(Object value){
    if (REGISTERED_OBJECTS.contains(value)) {
        throw new IllegalStateException("Object is already registered: " + value);
    }
    REGISTERED_OBJECTS.add(value);
}
}
