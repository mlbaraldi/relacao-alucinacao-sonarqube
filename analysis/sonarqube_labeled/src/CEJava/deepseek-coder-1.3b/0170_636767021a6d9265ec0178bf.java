package generated;
public class Generated58a97b4fc41b {
@Override protected Object convertToType(final Class<?> type,final Object value) throws Exception {
    if (value == null) {
        return null;
    }

    if (type.isInstance(value)) {
        return value;
    }

    if (type == Character.class) {
        if (value instanceof Character) {
            return value;
        } else if (value instanceof String && ((String) value).length() == 1) {
            return ((String) value).charAt(0);
        }
    }

    throw new Exception("Cannot convert " + value.getClass().getName() + " to " + type.getName());
}
}
