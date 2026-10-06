package generated;
public class Generated58a97b4fc41b {
@Override protected Object convertToType(final Class<?> type,final Object value) throws Exception {
    if (type == Character.class) {
        if (value instanceof Character) {
            return value;
        } else if (value instanceof String) {
            String str = (String) value;
            if (str.length() == 1) {
                return str.charAt(0);
            } else {
                throw new Exception("Cannot convert String of length greater than 1 to Character");
            }
        } else {
            throw new Exception("Cannot convert " + value.getClass().getName() + " to Character");
        }
    } else {
        throw new Exception("Cannot convert to " + type.getName());
    }
}
}
