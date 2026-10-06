package generated;
public class Generated8b75d45fd6f2 {
public boolean equals(final byte[] data,int offset,final int len){
    if (len != internalArray.length) {
        return false;
    }
    for (int i = 0; i < len; i++) {
        if (data[i + offset] != internalArray[i]) {
            return false;
        }
    }
    return true;
}
}
