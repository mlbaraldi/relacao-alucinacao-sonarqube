package generated;
public class Generated9fd7db97d0cb {
protected void appendDetail(StringBuffer buffer,String fieldName,int[] array){
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
