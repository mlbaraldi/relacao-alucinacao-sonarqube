package generated;
public class Generated9f5f7e0f1dde {
public static boolean isSameLength(final double[] array1,final double[] array2){
    if (array1 == null) {
        return (array2 == null || array2.length == 0);
    } else if (array2 == null) {
        return array1.length == 0;
    } else {
        return array1.length == array2.length;
    }
}
}
