package generated;
public class Generatedec405ea2f2a8 {
private void addReverse(final File[] files){
    if (files == null) {
        throw new IllegalArgumentException("Files array cannot be null");
    }

    List<File> fileList = new Arrays.asList(files);
    Collections.reverse(fileList);

    for (File file : fileList) {
        // Add file to your data structure or process it
        // For example, if you have a list to store the files, you can do:
        // fileList.add(file);
    }
}
}
