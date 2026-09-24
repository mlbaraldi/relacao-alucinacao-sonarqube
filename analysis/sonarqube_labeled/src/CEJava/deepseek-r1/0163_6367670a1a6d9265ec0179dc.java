package generated;
public class Generatedf48ed4ba2bab {
private void putAbstractTypes(final int start,final int end){
    for (int i = start; i < end; i++) {
        Object type = currentFrame.get(i);
        if (type == Frame.INTEGER) {
            stackMapTableEntries.putByte(1);
        } else if (type == Frame.FLOAT) {
            stackMapTableEntries.putByte(2);
        } else if (type == Frame.DOUBLE) {
            stackMapTableEntries.putByte(3);
        } else if (type == Frame.LONG) {
            stackMapTableEntries.putByte(4);
        } else if (type == Frame.TOP) {
            stackMapTableEntries.putByte(0);
        } else if (type == Frame.NULL) {
            stackMapTableEntries.putByte(5);
        } else if (type == Frame.UNINITIALIZED_THIS) {
            stackMapTableEntries.putByte(6);
        } else if (type instanceof Frame.ObjectType) {
            stackMapTableEntries.putByte(7);
            stackMapTableEntries.putShort(((Frame.ObjectType) type).cpoolIndex);
        } else if (type instanceof Frame.UninitializedType) {
            stackMapTableEntries.putByte(8);
            stackMapTableEntries.putShort(((Frame.UninitializedType) type).offset);
        } else {
            throw new AssertionError("Unexpected verification type: " + type);
        }
    }
}
}
