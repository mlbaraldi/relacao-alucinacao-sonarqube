package generated;
public class Generated413be13d5977 {
private static Object copyArrayGrow1(final Object array,final Class<?> newArrayComponentType){
    if (array == null) {
        try {
            return Array.newInstance(newArrayComponentType, 1);
        } catch (Exception e) {
            throw new IllegalArgumentException("Invalid array component type: " + newArrayComponentType);
        }
    }

    final int oldLength = Array.getLength(array);
    final Object newArray = Array.newInstance(array.getClass().getComponentType(), oldLength + 1);

    System.arraycopy(array, 0, newArray, 0, oldLength);

    return newArray;
}
}
