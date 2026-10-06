package generated;
public class Generated166528ab2bb6 {
@Override public void write(final byte b[],final int off,final int len) throws IOException {
    if (b == null) {
        throw new NullPointerException("b is null");
    }
    if (off < 0 || len < 0 || off + len > b.length) {
        throw new IndexOutOfBoundsException("Invalid offset or length");
    }
    if (len == 0) {
        return;
    }
    ensureCapacity(len);
    System.arraycopy(b, off, buf, count, len);
    count += len;
}
}
