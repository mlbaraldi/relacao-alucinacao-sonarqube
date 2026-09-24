package generated;
public class Generatedb94f6096aa70 {
final ByteVector put11(final int byteValue1,final int byteValue2){
    // Check if the vector needs to be enlarged
    if (size() < 2) {
        enlarge(2);
    }

    // Put the two bytes into the vector
    set(0, (byte) byteValue1);
    set(1, (byte) byteValue2);

    // Return the vector
    return this;
}
}
