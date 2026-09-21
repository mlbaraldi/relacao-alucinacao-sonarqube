package generated;
public class Generated413be13d5977 {
private static Object copyArrayGrow1(final Object array,final Class<?> newArrayComponentType){
    if (array == null) {
        return Array.newInstance(newArrayComponentType, 1);
    }

    int length = Array.getLength(array);
    Object newArray = Array.newInstance(newArrayComponentType, length + 1);
    System.arraycopy(array, 0, newArray, 0, length);
    return newArray;
}
}
