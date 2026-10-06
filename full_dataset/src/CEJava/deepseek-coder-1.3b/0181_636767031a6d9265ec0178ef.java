package generated;
public class Generated413be13d5977 {
private static Object copyArrayGrow1(final Object array,final Class<?> newArrayComponentType){
    if (array == null) {
        return Array.newInstance(newArrayComponentType, 1);
    }

    int originalSize = Array.getLength(array);
    @SuppressWarnings("unchecked")
    Object newArray = Array.newInstance(newArrayComponentType, originalSize + 1);
    System.arraycopy(array, 0, newArray, 0, originalSize);
    return newArray;
}
}
