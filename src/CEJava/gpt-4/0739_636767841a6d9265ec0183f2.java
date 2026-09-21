package generated;
public class Generated0aa471b272fd {
public int compare(Object aObj1,Object aObj2){
    // Check if both objects are Strings
    if (aObj1 instanceof String && aObj2 instanceof String) {
        String str1 = (String) aObj1;
        String str2 = (String) aObj2;

        // Use the String class's compareTo method
        return str1.compareTo(str2);
    } else {
        throw new IllegalArgumentException("Objects are not Strings");
    }
}
}
