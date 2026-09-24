package generated;
public class Generated13b86c0bee22 {
public byte[] toByteArray(){
    if (isEmpty()) {
        return new byte[0];
    }
    byte[] bytes = new byte[size()];
    for (int i = 0; i < size(); i++) {
        bytes[i] = get(i);
    }
    return bytes;
}
}
