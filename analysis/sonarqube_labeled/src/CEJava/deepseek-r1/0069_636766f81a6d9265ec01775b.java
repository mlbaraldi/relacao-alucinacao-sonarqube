package generated;
public class Generated157f4a2d9370 {
public long readLong(final int offset){
    byte[] buffer = this.buffer; // Assuming the ClassReader has a byte array named 'buffer'
    return ((buffer[offset]   & 0xFFL) << 56) |
           ((buffer[offset+1] & 0xFFL) << 48) |
           ((buffer[offset+2] & 0xFFL) << 40) |
           ((buffer[offset+3] & 0xFFL) << 32) |
           ((buffer[offset+4] & 0xFFL) << 24) |
           ((buffer[offset+5] & 0xFFL) << 16) |
           ((buffer[offset+6] & 0xFFL) << 8) |
           (buffer[offset+7]  & 0xFFL);
}
}
