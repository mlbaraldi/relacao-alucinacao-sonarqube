package generated;
public class Generated166528ab2bb6 {
@Override public void write(final byte b[],final int off,final int len) throws IOException {
    if (b == null) {
        throw new NullPointerException();
    }
    if (off < 0 || len < 0 || len > b.length - off) {
        throw new IndexOutOfBoundsException();
    }
    if (len == 0) {
        return;
    }

    int newCount = count + len;
    if (newCount > buf.length) {
        int oldCapacity = buf.length;
        int newCapacity = oldCapacity << 1;
        if (newCapacity < newCount) {
            newCapacity = newCount;
        }
        if (newCapacity < 0) {
            if (newCount < 0) {
                throw new OutOfMemoryError();
            }
            newCapacity = Integer.MAX_VALUE;
        }
        buf = Arrays.copyOf(buf, newCapacity);
    }

    System.arraycopy(b, off, buf, count, len);
    count = newCount;
}
}
