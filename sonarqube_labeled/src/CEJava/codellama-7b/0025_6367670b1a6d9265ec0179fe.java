package generated;
public class Generated072fc6a58d02 {
@Override public void write(byte b[]) throws IOException {
    if (b == null) {
        throw new NullPointerException("b is null");
    }
    if (b.length == 0) {
        return;
    }
    if (this.buf == null) {
        this.buf = new byte[b.length];
    }
    System.arraycopy(b, 0, this.buf, this.count, b.length);
    this.count += b.length;
}
}
