package generated;
public class Generated7b72b9475c1e {
public static char[] clone(final char[] array){
    if (array == null) {
        return null;
    }

    char[] clonedArray = new char[array.length];
    for (int i = 0; i < array.length; i++) {
        clonedArray[i] = array[i];
    }

    return clonedArray;
}
}
