package generated;
public class Generated413be13d5977 {
private static Object copyArrayGrow1(final Object array,final Class<?> newArrayComponentType){
    if (array == null) {
        return Array.newInstance(newArrayComponentType, 1);
    } else {
        int originalLength = Array.getLength(array);
        Class<?> componentType = array.getClass().getComponentType();
        Object newArray = Array.newInstance(componentType, originalLength + 1);
        System.arraycopy(array, 0, newArray, 0, originalLength);
        return newArray;
    }
}
}
