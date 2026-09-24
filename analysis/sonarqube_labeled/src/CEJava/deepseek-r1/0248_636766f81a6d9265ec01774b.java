package generated;
public class Generated43768aba827b {
public byte readByte() throws IOException {
    if (pos >= count) {
        count = in.read(buffer);
        pos = 0;
        if (count == -1) {
            throw new IOException("No more data available");
        }
    }
    return buffer[pos++];
}
}
