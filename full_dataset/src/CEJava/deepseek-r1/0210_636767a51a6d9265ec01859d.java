package generated;
public class Generated8b75d45fd6f2 {
public boolean equals(final byte[] data,int offset,final int len){
    if (internalData.length != len) {
        return false;
    }
    if (data == null) {
        return false;
    }
    if (offset < 0 || len < 0 || offset + len > data.length) {
        return false;
    }
    for (int i = 0; i < len; i++) {
        if (internalData[i] != data[offset + i]) {
            return false;
        }
    }
    return true;
}
}
