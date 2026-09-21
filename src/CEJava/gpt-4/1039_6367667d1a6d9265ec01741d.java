package generated;
public class Generated1f5a5c0e7b0c {
public static Type resolveBound(TypeVariable<?> typeVariable){
    Type[] bounds = typeVariable.getBounds();
    if (bounds.length == 0) {
        return Unknown.class;
    } else {
        return bounds[0];
    }
}
}
