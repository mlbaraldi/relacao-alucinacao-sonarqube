package generated;
public class Generated8cf1bc077b52 {
public Converter lookup(final Class<?> clazz){
    // Check if the class is already registered
    if (converters.containsKey(clazz)) {
        return converters.get(clazz);
    }

    // Check if the class has a registered converter
    for (Class<?> registeredClass : converters.keySet()) {
        if (registeredClass.isAssignableFrom(clazz)) {
            return converters.get(registeredClass);
        }
    }

    // If no converter is found, return null
    return null;
}
}
