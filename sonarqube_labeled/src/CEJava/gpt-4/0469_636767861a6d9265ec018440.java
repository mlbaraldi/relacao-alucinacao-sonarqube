package generated;
public class Generatede078462cf99f {
public void abbreviate(final int nameStart,final StringBuffer buf){
    String name = buf.substring(nameStart);
    String[] nameParts = name.split(" ");
    
    if (nameParts.length > 1) {
        buf.setLength(nameStart); // Reset the buffer to the start of the name
        buf.append(nameParts[0].charAt(0)); // Append the first letter of the first name
        buf.append(". ");
        buf.append(nameParts[1]); // Append the rest of the name after the first space
    }
}
}
