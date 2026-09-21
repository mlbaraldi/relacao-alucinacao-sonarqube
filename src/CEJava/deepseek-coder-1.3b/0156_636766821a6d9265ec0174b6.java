package generated;
public class Generated037dc8949432 {
public static Class<?>[] resolveArguments(Type genericType,Class<?> targetType){
    if (genericType instanceof ParameterizedType) {
        ParameterizedType parameterizedType = (ParameterizedType) genericType;
        Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();
        return resolveArguments(actualTypeArguments, targetType);
    } else if (genericType instanceof GenericArrayType) {
        GenericArrayType arrayType = (GenericArrayType) genericType;
        Type componentType = arrayType.getGenericComponentType();
        return new Class<?>[]{resolveArguments(componentType, targetType)[0]};
    } else {
        return new Class<?>[]{};
    }
}
}
