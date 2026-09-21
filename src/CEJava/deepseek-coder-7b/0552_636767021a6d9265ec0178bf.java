package generated;
public class Generated58a97b4fc41b {
@Override protected Object convertToType(final Class<?> type,final Object value) throws Exception {
    if (value == null) {
        return null;
    }

    if (type.equals(String.class)) {
        return value.toString();
    } else if (type.equals(Integer.class) || type.equals(int.class)) {
        if (value instanceof Number) {
            return ((Number) value).intValue();
        } else {
            throw new Exception("Cannot convert " + value.getClass().getName() + " to " + type.getName());
        }
    } else if (type.equals(Double.class) || type.equals(double.class)) {
        if (value instanceof Number) {
            return ((Number) value).doubleValue();
        } else {
            throw new Exception("Cannot convert " + value.getClass().getName() + " to " + type.getName());
        }
    } else if (type.equals(Character.class) || type.equals(char.class)) {
        if (value instanceof Character) {
            return value;
        } else if (value instanceof String && ((String) value).length() == 1) {
            return ((String) value).charAt(0);
        } else {
            throw new Exception("Cannot convert " + value.getClass().getName() + " to " + type.getName());
        }
    } else {
        throw new Exception("Unsupported type: " + type.getName());
    }
}
}
