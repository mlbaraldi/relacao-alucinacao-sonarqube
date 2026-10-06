package generated;
public class Generated178c4a579295 {
private static int decodeOctets(int i,ByteBuffer bb,StringBuilder sb){
    bb.position(i);
    while (bb.hasRemaining()) {
        int b = bb.get();
        if (b >= 0) {
            sb.append((char) b);
            i++;
        } else {
            int utf8Bytes = 0;
            if ((b >> 5) == -2) {
                utf8Bytes = 2;
            } else if ((b >> 4) == -2) {
                utf8Bytes = 3;
            } else if ((b >> 3) == -2) {
                utf8Bytes = 4;
            }
            if (bb.remaining() < utf8Bytes - 1) {
                break;
            }
            byte[] bytes = new byte[utf8Bytes];
            bytes[0] = (byte) b;
            for (int j = 1; j < utf8Bytes; j++) {
                bytes[j] = bb.get();
                i++;
            }
            String str = new String(bytes, "UTF-8");
            sb.append(str);
            i++;
        }
    }
    return i;
}
}
