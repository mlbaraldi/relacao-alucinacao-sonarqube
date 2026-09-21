package generated;
public class Generatede078462cf99f {
public void abbreviate(final int nameStart,final StringBuffer buf){
    String name = buf.substring(nameStart).trim();
    if (name.isEmpty()) {
        return;
    }
    String[] parts = name.split("\\s+");
    for (String part : parts) {
        if (!part.isEmpty()) {
            char initial = Character.toUpperCase(part.charAt(0));
            buf.append(initial);
        }
    }
}
}
