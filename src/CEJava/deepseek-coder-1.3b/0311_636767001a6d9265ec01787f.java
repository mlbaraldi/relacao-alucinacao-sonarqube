package generated;
public class Generated9fd7db97d0cb {
protected void appendDetail(StringBuffer buffer,String fieldName,int[] array){
    buffer.append(fieldName);
    buffer.append(" = [");

    for (int i = 0; i < array.length; i++) {
        buffer.append(array[i]);
        if (i < array.length - 1) {
            buffer.append(", ");
        }
    }

    buffer.append("];");
}
}
