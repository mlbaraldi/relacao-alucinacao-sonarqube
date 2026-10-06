package generated;
public class Generatedb94f6096aa70 {
final ByteVector put11(final int byteValue1,final int byteValue2){
    int currentLength = this.length;
    if (currentLength + 2 > data.length) {
        enlarge(2);
    }
    data[currentLength++] = (byte) byteValue1;
    data[currentLength++] = (byte) byteValue2;
    this.length = currentLength;
    return this;
}
}
