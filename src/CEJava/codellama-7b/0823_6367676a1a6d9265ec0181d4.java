package generated;
public class Generated6abb33d2b5b8 {
public static String[] addStringToArray(String[] array,String str){
    if (array == null) {
        array = new String[0];
    }
    String[] newArray = new String[array.length + 1];
    System.arraycopy(array, 0, newArray, 0, array.length);
    newArray[newArray.length - 1] = str;
    return newArray;
}
}
