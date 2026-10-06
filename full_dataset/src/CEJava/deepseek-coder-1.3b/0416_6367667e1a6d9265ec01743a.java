package generated;
public class Generatedbaec8ce15b2f {
public long lastWriteTimeStampInMilliseconds(){
    Path path = Paths.get("your_file_path"); // replace with your file path
    long lastModifiedTime = Files.getLastModifiedTime(path).toMillis();
    return Instant.now().minus(lastModifiedTime, ChronoUnit.MILLIS).toEpochMilli();
}
}
