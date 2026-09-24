package generated;
public class Generateda9beedb4f87d {
public int readTag() throws IOException {
    FileInputStream fis = new FileInputStream(filePath);
    int data = fis.read();
    fis.close();
    if (data == -1) {
        return 0; // return 0 if EOF is reached
    } else {
        return data; // return the read data
    }
}
}
