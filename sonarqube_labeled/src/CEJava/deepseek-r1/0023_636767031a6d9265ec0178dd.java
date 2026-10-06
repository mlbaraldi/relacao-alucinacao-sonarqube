package generated;
public class Generated460a86914965 {
public long contentLength(){
    String contentLength = getHeader("Content-Length");
    if (contentLength == null || contentLength.isEmpty()) {
        return -1;
    }
    try {
        return Long.parseLong(contentLength.trim());
    } catch (NumberFormatException e) {
        return -1;
    }
}
}
