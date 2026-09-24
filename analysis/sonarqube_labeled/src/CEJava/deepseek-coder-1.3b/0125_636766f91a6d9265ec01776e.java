package generated;
public class Generated166528ab2bb6 {
@Override public void write(final byte b[],final int off,final int len) throws IOException {
    if (off < 0 || len < 0 || off + len > b.length) {
        throw new IndexOutOfBoundsException();
    }
    if (len == 0) {
        return;
    }
    // Write the bytes to the underlying stream
    this.out.write(b, off, len);
}
}
