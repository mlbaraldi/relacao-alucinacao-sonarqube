package generated;
public class Generated037dc8949432 {
public static Class<?>[] resolveArguments(Type genericType,Class<?> targetType){
    // Check if genericType is instance of ParameterizedType
    if (genericType instanceof ParameterizedType) {
        ParameterizedType parameterizedType = (ParameterizedType) genericType;
        Type[] typeArguments = parameterizedType.getActualTypeArguments();

        // Check if targetType is assignable from all type arguments
        boolean isAssignable = Arrays.stream(typeArguments)
                .allMatch(type -> {
                    if (type instanceof Class<?>) {
                        return targetType.isAssignableFrom((Class<?>) type);
                    }
                    return false;
                });

        if (isAssignable) {
            return Arrays.stream(typeArguments)
                    .map(type -> (Class<?>) type)
                    .toArray(Class<?>[]::new);
        }
    }

    // Return null if genericType is not parameterized or if arguments cannot be resolved
    return null;
}
}
