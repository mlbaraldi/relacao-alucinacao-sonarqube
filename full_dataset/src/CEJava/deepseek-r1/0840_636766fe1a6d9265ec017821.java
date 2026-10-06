package generated;
public class Generated6fb3bbe6b4b4 {
protected void appendDetail(StringBuffer buffer,String fieldName,byte[] array){
    buffer.append('[');
    for (int i = 0; i < array.length; i++) {
        if (i > 0) {
            buffer.append(", ");
        }
        buffer.append(array[i]);
    }
    buffer.append(']');
}
}
