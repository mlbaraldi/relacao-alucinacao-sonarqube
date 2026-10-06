package generated;
public class Generated5b7588b58913 {
static String[] toNoNullStringArray(Object[] array){
    // Create a new array with the size of the original array
    String[] newArray = new String[array.length];
    int count = 0;

    // Iterate over the original array
    for(Object obj : array){
        // If the object is not null, add it to the new array
        if(obj != null){
            newArray[count] = (String) obj;
            count++;
        }
    }

    // Trim the new array to the correct size
    String[] trimmedArray = new String[count];
    System.arraycopy(newArray, 0, trimmedArray, 0, count);

    return trimmedArray;
}
}
