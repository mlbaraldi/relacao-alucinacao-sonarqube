package generated;
public class Generatede078462cf99f {
public void abbreviate(final int nameStart,final StringBuffer buf){
    // Check if the name is already short enough
    if (nameStart + 3 >= buf.length()) {
        return;
    }

    // Abbreviate the name by replacing the middle character with an abbreviation
    buf.replace(nameStart + 1, nameStart + 2, ".");
}
}
