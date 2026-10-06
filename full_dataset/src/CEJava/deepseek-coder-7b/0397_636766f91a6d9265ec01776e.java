package generated;
public class Generated166528ab2bb6 {
@Override public void write(final byte b[],final int off,final int len) throws IOException {
    if ((off < 0) || (off > b.length) || (len < 0) ||
        ((off + len) > b.length) || ((off + len) < 0)) {
        throw new IndexOutOfBoundsException();
    } else if (len == 0) {
        return;
    }

    if (count + len > buffer.length) {
        byte newBuffer[] = new byte[Math.max(count + len, 2 * buffer.length)];
        System.arraycopy(buffer, 0, newBuffer, 0, count);
        buffer = newBuffer;
    }

    System.arraycopy(b, off, buffer, count, len);
    count += len;
}
}
