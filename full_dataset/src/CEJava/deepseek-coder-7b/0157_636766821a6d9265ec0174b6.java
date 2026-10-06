package generated;
public class Generated037dc8949432 {
public static Class<?>[] resolveArguments(Type genericType,Class<?> targetType){
    if (genericType instanceof ParameterizedType) {
        ParameterizedType parameterizedType = (ParameterizedType) genericType;
        Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();
        Class<?>[] argumentClasses = new Class<?>[actualTypeArguments.length];
        for (int i = 0; i < actualTypeArguments.length; i++) {
            // This is a simplification. In a real-world scenario, you would need to handle
            // more complex cases, such as type variables and wildcard types.
            argumentClasses[i] = (Class<?>) actualTypeArguments[i];
        }
        return argumentClasses;
    }
    return null;
}
}
