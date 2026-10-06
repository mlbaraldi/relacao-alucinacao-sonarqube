package generated;
public class Generated6fb3bbe6b4b4 {
protected void appendDetail(StringBuffer buffer,String fieldName,byte[] array){
    if (buffer == null || array == null) {
        throw new IllegalArgumentException("buffer and array must not be null");
    }

    buffer.append("byte array: ");
    buffer.append(fieldName);
    buffer.append(" [");
    buffer.append(array.length);
    buffer.append("] = {");

    for (int i = 0; i < array.length; i++) {
        if (i > 0) {
            buffer.append(", ");
        }
        buffer.append(array[i]);
    }

    buffer.append("}");
}
}
