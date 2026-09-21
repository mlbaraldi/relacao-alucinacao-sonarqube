package generated;
public class Generated6576243044f8 {
@SuppressWarnings("unchecked") public static Supplier<String> createStringSupplier(int start){
    HashSet<String> uniqueStrings = new HashSet<>();
    int current = start;
    return () -> {
        String newString;
        do {
            newString = Integer.toString(current);
            current++;
        } while (uniqueStrings.contains(newString));
        uniqueStrings.add(newString);
        return newString;
    };
}
}
