package generated;
public class Generated43768aba827b {
public byte readByte() throws IOException {
    if (buffer.isEmpty()) {
        refillBuffer();
    }
    return buffer.removeFirst();
}
}
