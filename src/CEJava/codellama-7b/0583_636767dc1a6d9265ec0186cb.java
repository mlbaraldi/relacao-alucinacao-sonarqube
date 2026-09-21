package generated;
public class Generated6612173a2835 {
public void init(){
    // Check if the dist path is set
    if (distPath == null) {
        throw new IllegalArgumentException("Dist path is not set");
    }

    // Check if the dist path exists
    if (!new File(distPath).exists()) {
        throw new IllegalArgumentException("Dist path does not exist");
    }

    // Check if the dist path is a directory
    if (!new File(distPath).isDirectory()) {
        throw new IllegalArgumentException("Dist path is not a directory");
    }

    // Check if the dist path is writable
    if (!new File(distPath).canWrite()) {
        throw new IllegalArgumentException("Dist path is not writable");
    }

    // Check if the dist path is readable
    if (!new File(distPath).canRead()) {
        throw new IllegalArgumentException("Dist path is not readable");
    }

    // Check if the dist path is executable
    if (!new File(distPath).canExecute()) {
        throw new IllegalArgumentException("Dist path is not executable");
    }
}
}
