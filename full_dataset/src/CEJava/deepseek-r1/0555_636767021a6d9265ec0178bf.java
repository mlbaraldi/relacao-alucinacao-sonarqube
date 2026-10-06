package generated;
public class Generated58a97b4fc41b {
@Override protected Object convertToType(final Class<?> type,final Object value) throws Exception {
    // Check if the target type is Character or char
    if (type != Character.class && type != char.class) {
        throw new Exception("Conversion to " + type.getName() + " is not supported");
    }

    if (value == null) {
        return null;
    }

    if (value instanceof Character) {
        return value;
    }

    if (value instanceof CharSequence) {
        CharSequence cs = (CharSequence) value;
        if (cs.length() == 1) {
            return cs.charAt(0);
        } else {
            throw new Exception("CharSequence must be exactly one character long");
        }
    }

    if (value instanceof Number) {
        Number num = (Number) value;
        double doubleVal = num.doubleValue();
        long longVal = num.longValue();

        // Check if the numeric value is an integer
        if (doubleVal != longVal) {
            throw new Exception("Numeric value is not an integer");
        }

        // Check if the integer value is within the valid range for Character
        if (longVal < Character.MIN_VALUE || longVal > Character.MAX_VALUE) {
            throw new Exception("Numeric value " + longVal + " is out of Character range");
        }

        return (char) longVal;
    }

    throw new Exception("Cannot convert value of type " + value.getClass().getName() + " to Character");
}
}
