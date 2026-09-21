package generated;
public class Generated74eaaf0a8040 {
private static String javaCharset(String charset){
    switch (charset) {
        case "us-ascii":
            return "US-ASCII";
        case "iso-8859-1":
            return "ISO-8859-1";
        case "utf-8":
            return "UTF-8";
        case "utf-16":
            return "UTF-16";
        case "windows-1252":
            return "windows-1252";
        default:
            return charset; // Return the original name if no match found
    }
}
}
