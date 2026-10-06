package generated;
public class Generated037dc8949432 {
public static Class<?>[] resolveArguments(Type genericType,Class<?> targetType){
    if (!(genericType instanceof ParameterizedType)) {
        return null;
    }

    ParameterizedType parameterizedType = (ParameterizedType) genericType;
    Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();

    Class<?>[] resolvedArguments = new Class<?>[actualTypeArguments.length];
    for (int i = 0; i < actualTypeArguments.length; i++) {
        Type actualTypeArgument = actualTypeArguments[i];
        if (actualTypeArgument instanceof Class<?>) {
            resolvedArguments[i] = (Class<?>) actualTypeArgument;
        } else if (actualTypeArgument instanceof TypeVariable<?>) {
            TypeVariable<?> typeVariable = (TypeVariable<?>) actualTypeArgument;
            resolvedArguments[i] = resolveTypeVariable(typeVariable, targetType);
        } else {
            throw new IllegalArgumentException("Unsupported type argument: " + actualTypeArgument);
        }
    }

    return resolvedArguments;
}
}
