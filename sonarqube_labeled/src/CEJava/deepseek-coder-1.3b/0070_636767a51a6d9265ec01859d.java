package generated;
public class Generated8b75d45fd6f2 {
public boolean equals(final byte[] data,int offset,final int len){
    if (data.length - offset < len) {
        throw new IllegalArgumentException("Offset and length do not cover the entire array");
    }

    for (int i = 0; i < len; i++) {
        if (data[offset + i] != data[offset + len + i]) {
            return false;
        }
    }

    return true;
}
}
