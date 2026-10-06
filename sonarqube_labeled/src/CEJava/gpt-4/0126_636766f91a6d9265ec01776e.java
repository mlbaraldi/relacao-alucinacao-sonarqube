package generated;
public class Generated166528ab2bb6 {
@Override public void write(final byte b[],final int off,final int len) throws IOException {
    if ((off < 0) || (off > b.length) || (len < 0) || ((off + len) > b.length) || ((off + len) < 0)) {
        throw new IndexOutOfBoundsException();
    } else if (len == 0) {
        return;
    }
    for (int i = off; i < off + len; i++) {
        this.write(b[i]);
    }
}
}
