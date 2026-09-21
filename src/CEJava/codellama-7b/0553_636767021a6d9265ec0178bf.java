package generated;
public class Generated58a97b4fc41b {
@Override protected Object convertToType(final Class<?> type,final Object value) throws Exception {
    if (type == Character.class) {
        if (value instanceof String) {
            return ((String) value).charAt(0);
        } else if (value instanceof Character) {
            return value;
        } else {
            throw new Exception("Cannot convert value of type " + value.getClass().getName() + " to Character");
        }
    } else {
        throw new Exception("Cannot convert value of type " + value.getClass().getName() + " to " + type.getName());
    }
}
}
