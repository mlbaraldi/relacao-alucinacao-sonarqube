package generated;
public class Generateda9beedb4f87d {
public int readTag() throws IOException {
    int tag = 0;
    while (true) {
        int b = inputStream.read();
        if (b == -1) {
            return 0;
        }
        tag = (tag << 7) | (b & 0x7F);
        if ((b & 0x80) == 0) {
            return tag;
        }
    }
}
}
