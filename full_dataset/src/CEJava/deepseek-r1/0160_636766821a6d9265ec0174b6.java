package generated;
public class Generated037dc8949432 {
public static Class<?>[] resolveArguments(Type genericType,Class<?> targetType){
    if (!(genericType instanceof ParameterizedType)) {
        return null;
    }
    
    ParameterizedType parameterizedType = (ParameterizedType) genericType;
    Type rawType = parameterizedType.getRawType();
    if (!(rawType instanceof Class)) {
        return null;
    }
    
    Class<?> rawClass = (Class<?>) rawType;
    Type superType = getSuperType(targetType, rawClass);
    
    if (!(superType instanceof ParameterizedType)) {
        return null;
    }
    
    ParameterizedType superParameterizedType = (ParameterizedType) superType;
    Type[] actualTypeArguments = superParameterizedType.getActualTypeArguments();
    Class<?>[] resolvedArgs = new Class<?>[actualTypeArguments.length];
    
    for (int i = 0; i < actualTypeArguments.length; i++) {
        Class<?> resolved = resolveTypeToClass(actualTypeArguments[i], targetType);
        if (resolved == null) {
            return null;
        }
        resolvedArgs[i] = resolved;
    }
    
    return resolvedArgs;
}
}
