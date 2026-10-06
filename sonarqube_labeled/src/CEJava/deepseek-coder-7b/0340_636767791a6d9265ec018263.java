package generated;
public class Generated1f35586c2e8a {
private Class findClass(final String className) throws ClassNotFoundException {
    try {
        return Class.forName(className);
    } catch (ClassNotFoundException e) {
        throw new ClassNotFoundException("Class " + className + " not found");
    }
}
}
