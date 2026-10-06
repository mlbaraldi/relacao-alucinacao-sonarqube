package generated;
public class Generated43768aba827b {
public byte readByte() throws IOException {
    if (bufferPointer == bytesRead) {
        refill();
    }
    return buffer[bufferPointer++];
}
}
