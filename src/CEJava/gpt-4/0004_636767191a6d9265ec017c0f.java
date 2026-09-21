package generated;
public class Generateda9f5130099d4 {
private void enlarge(final int size){
    // Check if the data array needs to be enlarged
    if (data.length < size) {
        // Create a new array with the larger size
        byte[] newData = new byte[size];

        // Copy the existing data into the new array
        System.arraycopy(data, 0, newData, 0, data.length);

        // Replace the old array with the new one
        data = newData;
    }
}
}
