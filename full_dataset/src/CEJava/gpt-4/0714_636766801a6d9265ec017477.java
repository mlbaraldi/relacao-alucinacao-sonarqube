package generated;
public class Generated865b18762f92 {
private void addReverse(final InputStream[] files){
    if (files == null) {
        throw new IllegalArgumentException("Files cannot be null");
    }
    
    for (int i = files.length - 1; i >= 0; i--) {
        addFile(files[i]);
    }
}
}
