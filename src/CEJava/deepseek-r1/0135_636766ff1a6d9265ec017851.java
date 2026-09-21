package generated;
public class Generated88799e3adaeb {
protected int findByte(byte value,int pos){
    if (buffer == null || pos < 0 || pos >= buffer.length) {
        return -1;
    }
    for (int i = pos; i < buffer.length; i++) {
        if (buffer[i] == value) {
            return i;
        }
    }
    return -1;
}
}
