package generated;
public class Generated9fd7db97d0cb {
protected void appendDetail(StringBuffer buffer,String fieldName,int[] array){
    if (buffer == null || array == null) {
        throw new IllegalArgumentException("Buffer and array cannot be null");
    }

    buffer.append(fieldName + ": [");
    for (int i = 0; i < array.length; i++) {
        buffer.append(array[i]);
        if (i < array.length - 1) {
            buffer.append(", ");
        }
    }
    buffer.append("]");
}
}
