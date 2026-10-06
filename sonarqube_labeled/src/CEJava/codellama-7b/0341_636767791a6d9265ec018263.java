package generated;
public class Generated1f35586c2e8a {
private Class findClass(final String className) throws ClassNotFoundException {
    // Check if the class is already loaded
    Class<?> clazz = Class.forName(className);
    if (clazz != null) {
        return clazz;
    }

    // Try to load the class from the classpath
    try {
        clazz = Class.forName(className, true, Thread.currentThread().getContextClassLoader());
    } catch (ClassNotFoundException e) {
        // Class not found, try to load it from the system classloader
        clazz = Class.forName(className, true, ClassLoader.getSystemClassLoader());
    }

    if (clazz == null) {
        throw new ClassNotFoundException("Class " + className + " not found");
    }

    return clazz;
}
}
