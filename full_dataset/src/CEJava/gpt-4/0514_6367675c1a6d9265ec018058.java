package generated;
public class Generated6576243044f8 {
@SuppressWarnings("unchecked") public static Supplier<String> createStringSupplier(int start){
    counter = start;
    return () -> String.valueOf(counter++);
}
}
