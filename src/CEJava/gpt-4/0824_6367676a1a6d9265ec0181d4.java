package generated;
public class Generated6abb33d2b5b8 {
public static String[] addStringToArray(String[] array,String str){
    if (array == null) {
        return new String[] {str};
    } else {
        String[] newArray = new String[array.length + 1];
        System.arraycopy(array, 0, newArray, 0, array.length);
        newArray[array.length] = str;
        return newArray;
    }
}
}
