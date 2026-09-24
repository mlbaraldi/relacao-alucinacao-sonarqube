package generated;
public class Generated43768aba827b {
public byte readByte() throws IOException {
    if (position >= buffer.length) {
        throw new IOException("No more data available");
    }
    return buffer[position++];
}
}
