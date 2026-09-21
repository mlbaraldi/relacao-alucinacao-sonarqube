package generated;
public class Generateda9f5130099d4 {
private void enlarge(final int size){
    // Get the current length of the byte array
    int currentSize = this.length;

    // Create a new byte array with the enlarged size
    byte[] newArray = new byte[currentSize + size];

    // Copy the elements from the old array to the new array
    System.arraycopy(this, 0, newArray, 0, currentSize);

    // Replace the old array with the new array
    this = newArray;
}
}
